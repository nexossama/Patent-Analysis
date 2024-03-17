import json
from bson import ObjectId
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from search import search_title
app = Flask(__name__)
app.secret_key = "secret_key"  

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://aymanemaghouti:FwbFRrymX6wjJPxG@patents.js05fnq.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("patent_db")
users_collection = db.users
patents_collection = db.patent_records
user_records = db.user_records

def fetch_patents():
    mongodb_documents = []
    for patent in patents_collection.find({}):
        mongodb_documents.append(patent)
    return mongodb_documents

# todo
def fetch_panier(user):
    # Fetch all patents
    all_patents = fetch_patents()

    # Fetch patents selected by the user
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

        selected_patents = fetch_panier(user)

        return render_template('home.html', username=session['email'], all_patents=[], selected_patents=selected_patents)
    else:
            return render_template('login.html')


@app.route('/search_patents')
def search_patents():
    user_email = session['email']
    user = users_collection.find_one({'email': user_email})
    query = request.args.get('query', '')
    print(query)
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
    # Fetch patent details from the database based on the provided patent ID
    patent = patents_collection.find_one({'_id': ObjectId(patent_id)})

    if patent:
        patent['inventor_name'] = json.loads(patent['inventor_name'])
        patent['assignee_name_orig'] = json.loads(patent['assignee_name_orig'])
        patent['assignee_name_current'] = json.loads(patent['assignee_name_current'])
        return render_template('patent_details.html', patent=patent)
    else:
        # If patent is not found, render an error page or redirect to another route
        return render_template('error.html', message='Patent not found')




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
