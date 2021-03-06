from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from database import *
from datetime import *

app = Flask(__name__)
user_status = "%noneValue%"
username="%noneValue%"

@app.route('/', methods=["GET", "POST"])
def index():
    user_status = username
    #If the last time the page was loaded a timer was finished then get the timer tag
    if request.cookies.get("tag") != None:
        if request.cookies.get("user_status") != "" and request.cookies.get("user_status") != None:
            if request.cookies.get("timer_status") == "true" :
                append_value("analytics_data.json", request.cookies.get("user_status"), request.cookies.get("tag") + str(date.today()) + "%" + str(datetime.now().strftime("%H:%M:%S")))

 
    #When user enters a tag
    if request.method == "POST": 
        tag = request.form.get("tag")  
        return render_template("index.html", user=user_status, tag=tag)
    return render_template("index.html", user=user_status, tag="")

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
            return render_template("account_creation_failed.html")
    return render_template("create_account.html", user=user_status)


@app.route("/account", methods=["GET", "POST"])
def account () :
    password = ""
    i = 0
    #Search for username in login_data.json and get the equivilant password
    for line in open("login_data.json"):
            try :
                if read_value("login_data.json", i, "username") == request.cookies.get("user_status") :
                    password = read_value("login_data.json", i, "password")
            except :
                pass
            i = i + 1  
    return render_template("account.html", user=username, password_length=len(password))


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
            return render_template("login_failed.html")
    return render_template("login.html")


@app.route("/analytics")
def analytics() :
    username = request.cookies.get("user_status")
    try :
        return render_template("analytics.html", study_length_today=get_study_length_today("analytics_data.json", username), tags_today=get_tags_today("analytics_data.json", username), time_today=get_study_time_today("analytics_data.json", username), total_time=get_total_time_spent_today("analytics_data.json", username), longest_studied_time=get_most_productive_hour("analytics_data.json", username))
    except:
        return "You haven't spent any time focusing today!"

@app.route("/manifest.json")
def manifest() :
    return render_template("manifest.json")

app.run(debug=True, host='0.0.0.0')