from models.medico import Medico
from config import db

# Função para criar um novo Médico
def create_medico(nome, especialidade, crm):
    medico = Medico(nome=nome, especialidade=especialidade, crm=crm)
    db.session.add(medico)
    db.session.commit()

# Função para obter todos os Médicos
def get_medicos():
    return Medico.query.all()

# Função para obter um Médico por ID
def get_medico_by_id(medico_id):
    return Medico.query.get(medico_id)

# Função para atualizar um Médico
def update_medico(medico_id, nome=None, especialidade=None, crm=None):
    medico = Medico.query.get(medico_id)
    if nome:
        medico.nome = nome
    if especialidade:
        medico.especialidade = especialidade
    if crm:
        medico.crm = crm
    db.session.commit()

# Função para excluir um Médico
def delete_medico(medico_id):
    medico = Medico.query.get(medico_id)
    db.session.delete(medico)
    db.session.commit()
