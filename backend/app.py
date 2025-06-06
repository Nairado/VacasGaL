from flask import Flask
from extensions import db, migrate
from models import *
from os import getenv
from routes.usuario import bp as usuario_bp


def create_app():
    app = Flask(__name__)

    # PostgreSQL Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{password}@db:5432/{database}'.format(
        user=getenv('PSQL_USER'),
        password=getenv('PSQL_PSW'),
        database=getenv('PSQL_DB')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB and Migrations
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints registration
    app.register_blueprint(usuario_bp)

    return app


# Main entry point for the application
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=int(getenv('BCK_PORT', 5000)))