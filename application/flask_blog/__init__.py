from flask import Flask
from flask_login import LoginManager
import os

config = {
    'default': 'flask_blog.config.DevelopmentConfig',
    'development': 'flask_blog.config.DevelopmentConfig',
    'production': 'flask_blog.config.ProductionConfig'
}

app = Flask(__name__)
config_name = os.getenv('SERVERLESS_BLOG_CONFIG', 'default')
app.config.from_object(config[config_name])

login_manager = LoginManager()
login_manager.init_app(app)


login_manager.login_view = "login"
login_manager.login_message = "ログインしてください"
