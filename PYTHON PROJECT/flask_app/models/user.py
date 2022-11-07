print("model file running")

from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models.post import Post


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.user_name = data['user_name']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.post = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user"
        results = connectToMySQL('skate_schema').query_db(query)

        user = []
        for user in results:
            print(user)
            user.append(cls (user) )
        return user

    @classmethod
    def save(cls,data):
        query = "INSERT INTO user (first_name,last_name,email,password,user_name,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(user_name)s,NOW(),NOW());"
        new_user = connectToMySQL('skate_schema').query_db(query,data)
        return new_user

    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data["first_name"]) < 2:
            is_valid = False
            flash("First name needs 2 characters or more")
        
        if len(data["last_name"]) < 2:
            is_valid = False
            flash("Last name needs more than 2 characters")

        if len(data["email"]) < 1:
            is_valid = False
            flash("Add valid email")

        if len(data["user_name"]) < 1:
            is_valid = False
            flash("Add valid User Name")
        
        if len(data["password"]) < 8:
            is_valid = False
            flash("Password needs a min of 8 characters")

        if len(data["confirm"]) < 8:
            is_valid = False
            flash("Passwords must match")

        return is_valid

    @staticmethod
    def validate_login( login ):
        is_valid = True
        if not EMAIL_REGEX.match(login['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL('skate_schema').query_db(query,data)
        if len(results) < 1:
        # else:
            return False 
        #     print(result)  
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL('skate_schema').query_db(query,data)
        return results[0]

    @classmethod
    def update_info(cls,data):
        query ="UPDATE user SET first_name=%(first_name)s, last_name=%(last_name)s,email=%(email)s, user_name=%(user_name)s Where id=%(id)s;"
        connectToMySQL('skate_schema').query_db(query,data)
        print(query)

    @classmethod
    def get_user(cls,data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL('skate_schema').query_db(query,data)
        profile = cls(results[0])
        return profile

    @classmethod
    def get_users_post(cls,data):
        query = "Select * FROM user JOIN post on user.id = post.user_id; "
        results = connectToMySQL('skate_schema').query_db(query,data)
        one_user = results
        print(one_user)
        return results




    @classmethod
    def get_by_names(cls,data):
        query = "SELECT * FROM user JOIN post ON post.user_id = user.id WHERE post.id = %(id)s;"
        results = connectToMySQL('skate_schema').query_db(query,data)
        return results




