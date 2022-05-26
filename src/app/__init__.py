from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Globally Accessible Libraries
db = SQLAlchemy()
mg = Migrate()

def init_app():
    """ Inits the core application. """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Init Plugins
    db.init_app(app)
    mg.init_app(app, db)

    with app.app_context():
        # Incldue the routes and blueprints
        from .home import routes as home
        from .entries import routes as entries

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(entries.entries_bp)

        return app