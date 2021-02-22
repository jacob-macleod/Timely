from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from database import *

app = Flask(__name__)
user_status = "%noneValue%"
username="%noneValue%"

@app.route('/')
def index():
    user_status = username
    return render_template("index.html", user=user_status)

@app.route("/create_account", methods=["GET", "POST"])
def create_account() :
    global username
    if request.method == "POST": 
        global username
        old_username = username
        # Get username and pasword
        username = request.form.get("uname") 
        password = request.form.get("pword")  
        password_confirm = request.form.get("pword_confirm")

        #If the password an password confirmation matches
        if password == password_confirm :
            #Save to login_data.json
            append_value("login_data.json", username, password)
            return render_template("account_confirmation.html", user=username)
        else :
            username = old_username
            return "Try again! Your password and username don't match!"
    return render_template("create_account.html", user=user_status)


@app.route("/login", methods=["GET", "POST"])
def login () :
    logged_in = False
    global username
    old_username = username
    i = 0
    if request.method == "POST":
        username = request.form.get("uname") 
        password = request.form.get("pword")

        #Search for username in login_data.json
        for line in open("login_data.json"):
            try :
                if read_value("login_data.json", i, "username") == username and read_value("login_data.json", i, "password"):
                    #Log user in
                    user_status = username 
                    logged_in = True
                    return render_template("login_confirmation.html", user=username)
            except :
                pass
            i = i + 1  
        #If the user's password/username is wrong
        if (logged_in == False) :
            username = old_username
            return "Sorry, your login details didn't work"
    return render_template("login.html")

app.run(debug=True, host='0.0.0.0')