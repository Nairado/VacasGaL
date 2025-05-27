from flask import Flask
from extensions import db, migrate
from models import *
from os import getenv
from routes.usuario import bp as usuario_bp

app = Flask(__name__)

# PostgreSQL DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{password}@db:5432/{database}'.format(
    user=getenv('PSQL_USER'),
    password=getenv('PSQL_PSW'),
    database=getenv('PSQL_DB')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB y Migraciones
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(getenv('BCK_PORT', 5000)))
