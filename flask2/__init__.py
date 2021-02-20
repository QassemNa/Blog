import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask2.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manger = LoginManager()
login_manger.login_view = 'users.login'
login_manger.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manger.init_app(app)
    login_manger.init_app(app)
    login_manger.init_app(app)
    mail.init_app(app)

    from flask2.users.routes import users
    from flask2.posts.routes import posts
    from flask2.main.routes import main
    from flask2.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app