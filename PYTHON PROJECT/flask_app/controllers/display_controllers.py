print("controller file running")

from crypt import methods
from re import template
from flask import render_template,redirect,request,session, Flask,flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask_app.api import find_shops
bcrypt = Bcrypt(app) 



@app.route("/")
def display_page():
    return render_template("display.html")

app.route("/")
def return_home():

    return render_template("display.html")

@app.route("/skate/submit",methods=['post'])
def locate_shop():
    data = {
        "location":request.form["location"],
        "text":request.form["text"]

    }
    print('data',data)

    # shops = find_shops(data['location'])
    print("here are the shops")
    session['data'] = data
    # print(shops)
    # print(data['location'])

    return redirect ("/skate")

@app.route("/skate")
def skate_shop():
    # data = {
    data = session['data']
        # "text":session["data"],
        # "location":session["data"],
    #     # "find_shops": {"location":location,"text":text}

    # }
    
    print("here are the shops")
    shops = find_shops("skateboard",data['location'])
    print(shops['businesses'])
    
    return render_template("skate.html",shops=shops['businesses'])

@app.route("/park/submit",methods=['post'])
def park_location():
    data = {
        "location":request.form["location"],
        "park":request.form["park"]

    }
    print("here are the shops")
    session['data'] = data
    return redirect("/park")

@app.route("/park")
def park():
    data = session['data']
    
    print("here are the shops")
    parks = find_shops("park",data['location'])
    
    return render_template("park.html",parks=parks['businesses'])

@app.route("/login")
def login_page():
    return render_template("/login.html")

@app.route("/login",methods=['post'])
def login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/login")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect("/")

    session['new_user'] = user_in_db.id
    return redirect ("/dashboard")


@app.route("/register/account")
def register_page():
    return render_template("registration.html")

@app.route("/register/submit",methods=['post'])
def register_account():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "user_name":request.form["user_name"],
        "password": request.form["password"],
        "confirm": request.form["confirm"]
    }
    if not User.validate_user(data):
        return redirect("/register/account")

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data["password"] = pw_hash

    new_user=User.save(data)
    session["user"] = new_user
    print(f"new user is {new_user}")
    return render_template("registrationConfirmation.html")

