from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['post'])
def signup():
    username = request.form['username']

    # error "That's not a valid username"
    # error "That's not a valid password"
    # error "Passwords don't match"
    # error "That's not a valid email"
    
    return render_template('welcome.html',
        username = username)

app.run()