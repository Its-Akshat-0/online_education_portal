from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    # Initialize DB
    db.init_app(app)

    # Import blueprints *after* db is set up
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
