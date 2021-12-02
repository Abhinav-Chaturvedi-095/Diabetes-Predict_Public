#to make this folder a python package 

from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_login import login_required

db = SQLAlchemy()
DB_NAME = "database.db"
app = Flask(__name__)

def create_app():
    # app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld" #USE FOR HASH IN SESSIONS
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from views import views  #for relative import
    from auth import auth      #for relative import
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")
        
if __name__ == "__main__":
    create_app()
    app.run(debug=True)