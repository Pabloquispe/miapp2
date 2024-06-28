import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config_by_name

from controladores.admin_routes import admin_bp
from controladores.user_routes import user_bp
from controladores.auth_routes import auth_bp
from controladores.main_routes import main_bp

db = SQLAlchemy()

def create_app(config_name):
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__, template_folder='vistas/templates', static_folder='vistas/static')
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=(app.config['DEBUG']))

