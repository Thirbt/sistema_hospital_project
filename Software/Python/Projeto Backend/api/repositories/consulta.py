from models.consulta import Consulta
from config import db

def create_consulta(data, horario, descricao):
    consulta = Consulta(data=data, horario=horario, descricao=descricao)
    db.session.add(consulta)
    db.session.commit()
    
def get_consulta():
    return Consulta.query.all()

def get_consulta_by_id(consulta_id):
    return Consulta.query.get(consulta_id)

def update_consulta(consulta_id, data=None, horario=None, descricao=None):
    consulta = Consulta.query.get(consulta_id)
    if data:
        consulta.data = data
    if horario:
        consulta.horario = horario
    if descricao:
        consulta.descricao = descricao
    db.session.commit()
    
def delete_consulta(consulta_id):
    consulta = Consulta.query.get(consulta_id)
    db.session.delete(consulta)
    db.session.commit()

    