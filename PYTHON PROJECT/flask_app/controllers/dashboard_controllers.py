print("controller file running")

from crypt import methods
from re import template
from flask import render_template,redirect,request,session, Flask,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post


@app.route("/dashboard")
def dashboard_page():
    if "new_user" not in session:
        return redirect('/')
    data = {
        "id": session["new_user"]
    }
    edit_user = User.get_user(data)

    posts=User.get_users_post(data)

    user_in_db = User.get_by_id(data)
    return render_template("dashboard.html",user_in_db=user_in_db,posts=posts,edit_user=edit_user)

@app.route("/logout")
def logout():
    return redirect("/login")

@app.route("/add")
def add_page():
    return render_template("addPost.html")

@app.route("/add/post",methods=['post'])
def add_post():
    data ={
        "comment":request.form["comment"],
        "image":request.form["image"],
        "user_id":session["new_user"]
    }
    new_post= Post.create(data)
    print(f"new post added{new_post}")
    return redirect("/dashboard")

@app.route("/edit/<int:id>")
def edit(id):
    data ={
        "id":session['new_user']
    }
    edit_user = User.get_by_id(data)

    return render_template("edit.html")

@app.route("/edit",methods=['post'])
def edit_user():
    data = {
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "user_name":request.form["user_name"],
    }
    update_info = User.update_info(data)

    return redirect("/dashboard")

@app.route("/view/<int:id>")
def view_page(id):
    data = {
        "id":id
    }
    user_post=User.get_by_names(data)
    return render_template("viewPost.html",user_post=user_post)

@app.route("/message")
def message_user():
    return 'you are going to message the user'