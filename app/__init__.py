from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootsrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    bootsrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # will add views and forms

    return app