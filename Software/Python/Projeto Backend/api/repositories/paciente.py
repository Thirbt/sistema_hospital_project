from models.paciente import Paciente
from config import db

def create_paciente(nome, idade):
    paciente = Paciente(nome = nome, idade = idade)
    db.session.add(paciente)
    db.session.commit()
    
def get_pacientes():
    return Paciente.query.all()

def get_paciente_by_id(paciente_id):
    return Paciente.query.get(paciente_id)

def update_paciente(paciente_id, nome=None, idade=None):
    paciente = Paciente.query.get(paciente_id)
    if nome:
        paciente.nome = nome
    if idade:
        paciente.idade = idade
    db.session.commit()

def delete_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    db.session.delete(paciente)
    db.session.commit()