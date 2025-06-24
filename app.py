from flask import Flask
from extensions import db, cors, swagger
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger

from models.medico import Medico
from models.paciente import Paciente
from models.consulta import Consulta

from controllers.medico import medico_bp
from controllers.paciente import paciente_bp
from controllers.consulta import consulta_bp

app = Flask(__name__)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8080
app.config['DEBUG'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

app.config['SWAGGER'] = {
    'title': 'API de Consultas Médicas',
    'uiversion': 3,
    'specs_route': '/apidocs/',
    'swagger_ui_bundle_config': {
        'docExpansion': "list",
        'filter': True,
        'displayRequestDuration': True,
    },
    'info': {
        'title': 'API de Consultas Médicas',
        'version': '1.0',
        'description': 'Documentação da API de gerenciamento de pacientes, médicos e consultas.',
        'contact': {
            'github': 'Thirbt'
        }
    },
    'tags': [
        {'name': 'Pacientes', 'description': 'Operações relacionadas a pacientes'},
        {'name': 'Médicos', 'description': 'Operações relacionadas a médicos'},
        {'name': 'Consultas', 'description': 'Operações relacionadas a consultas'}
    ]
}

db.init_app(app)
cors.init_app(app, origins=["*"])
swagger.init_app(app)

app.register_blueprint(medico_bp)
app.register_blueprint(paciente_bp)
app.register_blueprint(consulta_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()    
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])