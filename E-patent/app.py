import json
from bson import ObjectId
from configparser import ConfigParser
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from pymongo import MongoClient
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from search import search_title
app = Flask(__name__)


app.secret_key = "secret_key"  

client = MongoClient("mongodb+srv://aymanemaghouti:FwbFRrymX6wjJPxG@patents.js05fnq.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("patent_db")


# Access the google_patents collection
patents_collection = db.google_patents

users_collection = db.users
user_records = db.user_records

def fetch_patents():
    mongodb_documents = []
    for patent in patents_collection.find({}):
        mongodb_documents.append(patent)
    return mongodb_documents

def fetch_total_patents_count(keyword):
    # total_documents_count = patents_collection.count_documents({})
    query = {"title": {"$regex": keyword, "$options": "i"}}
    total_documents_count = patents_collection.count_documents(query)
    return total_documents_count

# todo
def fetch_panier(user):
    all_patents = fetch_patents()

    selected_patents = []
    for patent in all_patents:
        for patent_id in user.get('patents', []):
            if str(patent['_id']) == str(patent_id):
                selected_patents.append(patent)
    return selected_patents


@app.route('/')
def home():
    if 'email' in session:
        user_email = session['email']
        user = users_collection.find_one({'email': user_email})

        # selected_patents = fetch_panier(user)
        selected_patents = []

        return render_template('home.html', patents=[], selected_patents=selected_patents)
    else:
        return render_template('login.html')


@app.route('/insight')
def insight():
    if 'email' in session:
        user_email = session['email']
        user = users_collection.find_one({'email': user_email})

        return render_template('insight.html', username=session['email'])
    else:
        return render_template('login.html')    


@app.route('/search_patents')
def search_patents():
    user_email = session['email']
    user = users_collection.find_one({'email': user_email})
    selected_patents = fetch_panier(user)
    
    per_page = 5
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * per_page
    
    query = request.args.get('query', '')
    patent_items = search_title(query, offset, per_page)
    total_patents_count = fetch_total_patents_count(query)
    total_pages = (total_patents_count + per_page - 1) // per_page
    
    patents = {
        'patent_items': patent_items,
        'selected_patents': selected_patents,
        'total_patents_count': total_patents_count
    }

    return render_template('home.html', patents=patents, page=page,
                            total_pages=total_pages, query=query)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'email' in session:
        user_email = session['email']
        user = users_collection.find_one({'email': user_email})
        if user:
            record_id = request.json['record_id']
            users_collection.update_one(
                {'email': user_email},
                {'$addToSet': {'patents': record_id}}
            )
            return jsonify({'message': 'Record added to cart successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'User not logged in'}), 401


@app.route('/delete_patent', methods=['POST'])
def delete_patent():
    if 'email' in session:
        user_email = session['email']
        user = users_collection.find_one({'email': user_email})
        if user:
            record_id = request.json['record_id']
            print(ObjectId(record_id))
            users_collection.update_one(
                {'email': user_email},
                {'$pull': {'patents': str(record_id)}}
            )
            return jsonify({'message': 'Patent deleted successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'User not logged in'}), 401


@app.route('/patent/<patent_id>')
def patent_details(patent_id):
    print(patent_id)
    patent = patents_collection.find_one({'_id': ObjectId(patent_id)})
    print(patent)

    if patent:

        if patent['source'] == 'google patenffft':

            patent['inventor_name'] = json.loads(patent['inventor_name'])
            patent['assignee_name_orig'] = json.loads(patent['assignee_name_orig'])
            patent['assignee_name_current'] = json.loads(patent['assignee_name_current'])

        return render_template('patent_details.html', patent=patent)
    else:
        # If patent is not found, render an error page or redirect to another route
        return render_template('patent_details.html', message='Patent not found')




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email-I']
        password = request.form['password1-I']
        username = request.form['username-I']

        existing_user = users_collection.find_one({'email': email})
        if existing_user:
            return 'That email already exists!'

        hash_pass = generate_password_hash(password)
        users_collection.insert_one({'username':username ,'email': email, 'password': hash_pass})
        session['email'] = email
        session['username']=username
        return redirect('/')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email-C']
        password = request.form['password-C']

        existing_user = users_collection.find_one({'email': email})
        if existing_user and check_password_hash(existing_user['password'], password):
            session['email'] = email
            return redirect('/')
        return 'Invalid email/password combination'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        # Extracting selected filters
        search_terms = request.form.getlist('search_terms')
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        source = request.form.getlist('source')
        patent_office = request.form.get('patent_office')

        print(search_terms)
        print(source)
        
        # Building the SQL query
        query = "SELECT * FROM patents WHERE 1=1"

        # Adding serach_terms filter
        if search_terms:
            search_terms = "','".join(search_terms)
            query += f" AND source IN ('{search_terms}')"
        
        # Adding year range filter
        if start_year:
            query += f" AND year >= {start_year}"
        if end_year:
            query += f" AND year <= {end_year}"
        
        # Adding source filter
        if source:
            sources = "','".join(source)
            query += f" AND source IN ('{sources}')"
        
        # Adding patent office filter
        if patent_office:
            query += f" AND patent_office = '{patent_office}'"
        
        # Execute the query (this part is a placeholder, adjust based on your database setup)
        # results = execute_query(query)
        
        # Return the query for demonstration purposes
        return query


if __name__ == '__main__':
    app.run(debug=True)
