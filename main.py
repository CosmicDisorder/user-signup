from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():

        return render_template('index.html')

@app.route("/", methods=['post'])
def signup():
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        vpassword = request.form['verify_password']

        user_error = ''
        pass_error = ''
        vpass_error = ''
        email_error = ''

        if username == '':
                user_error = "That's not a valid username"
        if len(username) < 3 or len(username) > 20:
                user_error = "That's not a valid username"

        if email != '':
                if len(email) < 3 or len(email) > 20:
                        email_error = "That is not a valid email"

                num_at = 0
                num_dot = 0
                
                print("checking for number of @ and .\n")
                for char in email:
                        if char == '@':
                                num_at += 1
                
                        if char == '.':
                                num_dot += 1

                        if num_at > 1 or num_dot > 1:
                                email_error = "That is not a valid email"

                        if char == ' ':
                                email_error = "That is not a valid email"

                if num_at != 1 and num_dot != 1:
                        email_error = "That is not a valid email"
                else:
                        char_position = 0
                        characters_since_at = 0
                        at_exists = False
                        characters_since_dot = 0
                        dot_exists = False
                        for i in email:
                                if at_exists:
                                        characters_since_at += 1
                                if dot_exists:
                                        characters_since_dot += 1
                                if i == '@':
                                        at_exists = True
                                if i == '.':
                                        dot_exists = True
                                if dot_exists and at_exists:
                                        if characters_since_at < 2:
                                                email_error = "That is not a valid email"
                                if i == '.' and char_position == len(email):
                                        email_error = "That is not a valid email"
                                char_position += 1

        if password == '':
                pass_error = "That's not a valid password"

        if password != vpassword:
                vpass_error = "Passwords don't match"

        if user_error == pass_error and user_error == vpass_error and user_error == email_error:
                return render_template('welcome.html', username=username)
        else:
                return render_template('index.html',
                        username = username, email = email, 
                        user_error = user_error, pass_error = pass_error,
                        vpass_error = vpass_error, email_error = email_error)
                

app.run()