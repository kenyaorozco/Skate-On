print("model file running")

from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
    def __init__( self , data ):
        self.id = data['id']
        self.comment = data['comment']
        self.image = data['image']
        self.user_id = data['user_id']
        self.user= None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM post JOIN user ON user.id = post.user_id;"
        results = connectToMySQL('skate_schema').query_db(query)

        posts = []
        for post in results:
            single_post = cls(post)
            user_data = {
                "id":post["user.id"],
                "first_name":post["first_name"],
                "last_name":post["last_name"],
                "email":post["email"],
                "user_name":post["user_name"],
                "password":post["password"],
            }
        single_post.user=User(user_data)
        posts.append( single_post)
        return posts

    @classmethod
    def create(cls,data):
        query="Insert into post (comment,image,user_id) VALUES (%(comment)s,%(image)s,%(user_id)s);"
        new_post = connectToMySQL('skate_schema').query_db(query,data)
        return new_post


