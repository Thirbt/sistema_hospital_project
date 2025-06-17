from models.consulta import Consulta
from models.medico import Medico
from models.paciente import Paciente
from extensions import db
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from utilities.utility import is_valid_input_string, is_valid_string_date


def create_consulta(data, horario, descricao, paciente_id, medico_id):
    if not paciente_id:
      return jsonify({"message": "O ID do paciente é obrigatório para a criação de uma consulta!"}), 400  
  
    if not medico_id:
      return jsonify({"message": "O ID do médico é obrigatório para a criação de uma consulta!"}), 400  
    
    if not isinstance(data, str) or not is_valid_string_date(data):
        return jsonify({"message": "Formato de data inválido. Use 'dd/mm/YYYY' como string."}), 400
    
    if not all(param is not None and is_valid_input_string(param) for param in [data, horario, descricao]):
        return jsonify({"message": "Dados inválidos para criação de uma consulta!"}), 400
    
    try:
        paciente = db.session.get(Paciente, paciente_id)
        if not paciente:
            return jsonify({"message": f"O paciente com ID {paciente_id} não foi encontrado!"}), 404
        medico = db.session.get(Medico, medico_id)
        if not medico:
            return jsonify({"message": f"O médico com ID {medico_id} não foi encontrado!"}), 404
        consulta = Consulta(data = data, horario = horario, descricao = descricao, paciente_id = paciente_id, medico_id = medico_id)
        db.session.add(consulta)
        db.session.commit()
        return jsonify({"message": "Consulta criada com sucesso!"}), 201
    except IntegrityError as integrity_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de integridada ao criar consulta: {str(integrity_error)}"}), 409
    except SQLAlchemyError as sqlalchemy_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de banco de dados ao criar consulta: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        db.session.rollback()
        return jsonify({"message": f"Erro inesperado ao criar consulta: {str(exception)}"}), 500
    
def get_consulta():
    try:
        consultas = Consulta.query.all()
        return jsonify([consulta.to_dict() for consulta in consultas]), 200
    except SQLAlchemyError as sqlalchemy_error:
        return jsonify({"message": f"Erro de banco de dados ao buscar consultas: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        return jsonify({"message": f"Erro inesperado ao buscar consultas: {str(exception)}"}), 500

def get_consulta_by_id(consulta_id):
    if not consulta_id:
        return jsonify({"message": "Informe o ID da consulta!"}), 400
    try:
        consulta = db.session.get(Consulta, consulta_id)
        if not consulta:
            return jsonify({"message": f"A consulta com ID {consulta_id} não foi encontrada!"}), 404
        return jsonify(consulta.to_dict()), 200
    except SQLAlchemyError as sqlalchemy_error:
        return jsonify({"message": f"Erro de banco de dados ao buscar consulta: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        return jsonify({"message": f"Erro inesperado ao buscar consulta: {str(exception)}"})

def update_consulta(consulta_id, data, horario, descricao, paciente_id, medico_id):
    if not paciente_id:
      return jsonify({"message": "O ID do paciente é obrigatório para a criação de uma consulta!"}), 400  
  
    if not medico_id:
      return jsonify({"message": "O ID do médico é obrigatório para a criação de uma consulta!"}), 400  
  
    if not isinstance(data, str) or not is_valid_string_date(data):
        return jsonify({"message": "Formato de data inválido. Use 'dd/mm/YYYY' como string."}), 400
    
    if not all(param is not None and is_valid_input_string(param) for param in[data, horario, descricao]):
        return jsonify({"message": "Dados inválidos para atualizar consulta!"}), 400
    
    
    try:
        paciente = db.session.get(Paciente, paciente_id)
        if not paciente:
            return jsonify({"message": f"O paciente com ID {paciente_id} não foi encontrado!"}), 404
        medico = db.session.get(Medico, medico_id)
        if not medico:
            return jsonify({"message": f"O médico com ID {medico_id} não foi encontrado!"}), 404
        consulta = db.session.get(Consulta, consulta_id)
        if not consulta:
            return jsonify({"message": f"A consulta com ID {consulta_id} não foi encontrada!"}), 404
        consulta.data = data
        consulta.horario = horario
        consulta.descricao = descricao
        consulta.paciente_id = paciente_id
        consulta.medico_id = medico_id
        db.session.commit()
        return jsonify({"message": "Consulta atualiza com sucesso!"}), 200
    except IntegrityError as integrity_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de integridade ao atualizar consulta: {str(integrity_error)}"}), 409
    except SQLAlchemyError as sqlalchemy_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de banco de dados ao atualizar consulta: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        db.session.rollback()
        return jsonify({"message": f"Erro inesperado ao atualizar consulta: {str(exception)}"}), 500
    
def delete_consulta(consulta_id):
    if not consulta_id:
        return jsonify({"message": "Informe o ID da consulta!"}), 400
    try:
        consulta = db.session.get(Consulta, consulta_id)
        if not consulta:
            return jsonify({"message": f"A consulta com ID {consulta_id} não foi encontrada!"}), 404
        db.session.delete(consulta)
        db.session.commit()
        return jsonify({"message": "Consulta deletada com sucesso!"}), 200
    except SQLAlchemyError as sqlalchemy_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de banco de dados ao deletar a consulta: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        db.session.rollback()
        return jsonify({"message": f"Erro inesperado ao deletar consulta: {str(exception)}"}), 500

    