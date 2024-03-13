from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'indexx'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_signin/signup()"
    else:
        return render_template('login.html')

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


if __name__ == '__main__':
    app.run(debug=True)