import json
from bson import ObjectId
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from pymongo import MongoClient
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


previous = 1
page = 2
nbrPages = 5
next = 3
rowNbr = 10

@app.route('/')
def home():
    if 'email' in session:
        user_email = session['email']
        user = users_collection.find_one({'email': user_email})

        selected_patents = fetch_panier(user)

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
    query = request.args.get('query', '')
    search_results = search_title(query)
    selected_patents = fetch_panier(user)
    return render_template('home.html', all_patents=search_results,selected_patents=selected_patents)




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


if __name__ == '__main__':
    app.run(debug=True)
