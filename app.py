from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret_key"  

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://aymanemaghouti:FwbFRrymX6wjJPxG@patents.js05fnq.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("patent_db")
users_collection = db.users
patents_collection = db.patent_records

def fetch_patents():
    mongodb_documents = []
    for patent in patents_collection.find({}):
        mongodb_documents.append(patent)
    return mongodb_documents

# todo
def fetch_panier(user):
    mongodb_documents = []
    for panier in user:
        mongodb_documents.append(panier)
    return mongodb_documents

@app.route('/')
def home():
    if 'email' in session:
        mongodb_documents = fetch_patents()
        return render_template('home.html', username=session['email'], mongodb_documents=mongodb_documents)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email-I']
        password = request.form['password1-I']

        existing_user = users_collection.find_one({'email': email})
        if existing_user:
            return 'That email already exists!'

        hash_pass = generate_password_hash(password)
        users_collection.insert_one({'email': email, 'password': hash_pass})
        session['email'] = email
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

if __name__ == '__main__':
    app.run(debug=True)
