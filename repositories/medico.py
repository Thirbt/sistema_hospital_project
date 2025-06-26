from models.medico import Medico
from models.consulta import Consulta
from extensions import db
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from utilities.utility import is_valid_input_string

def create_medico(nome, especialidade, crm):
    if not all(param is not None and is_valid_input_string(param) for param in [nome, especialidade, crm]):
        return jsonify({"message": "Dados inválidos para a criação de um médico!"}), 400
    try:
        medico = Medico(nome = nome, especialidade = especialidade, crm = crm)
        db.session.add(medico)
        db.session.commit()
        return jsonify({"message": f"Médico {nome} foi criado com sucesso!"}), 201
    except IntegrityError as integrity_error:
        db.session.rollback()
        if "UNIQUE constraint failed: medicos.crm" in str(integrity_error):
            return jsonify({"message": "Erro de integridade: CRM já cadastrado para outro médico."}), 409
        return jsonify({"message": f"Erro de integridade ao criar médico: {str(integrity_error)}"}), 409
    except SQLAlchemyError as sqlalchemy_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de banco de dados ao criar médico: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        db.session.rollback()
        return jsonify({"message": f"Erro inesperado ao criar médico: {str(exception)}"}), 500

def get_medicos():
    try:
        medicos = Medico.query.all()
        return jsonify([medico.to_dict() for medico in medicos]), 200
    except SQLAlchemyError as sqlalchemy_error:
        return jsonify({"message": f"Erro de banco de dados ao buscar médicos: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        return jsonify({"message": f"Erro inesperado ao buscar médicos: {str(exception)}"}), 500

def get_medico_by_id(medico_id):
    if not medico_id:
        return jsonify({"message": "Informe o ID do médico!"}), 400
    try:
        medico = db.session.get(Medico, medico_id)
        if not medico:
            return jsonify({"message": f"Médico com ID {medico_id} não foi encontrado!"}), 404
        return jsonify(medico.to_dict()), 200
    except SQLAlchemyError as sqlalchemy_error:
        return jsonify({"message": f"Erro de banco de dados ao buscar médico: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        return jsonify({"message": f"Erro inesperado ao buscar médico: {str(exception)}"}), 500

def update_medico(medico_id, nome, especialidade, crm):
    if not medico_id:
        return jsonify({"message": "ID do médico é obrigatório para a atualização!"}), 400
    
    if not all(param is not None and is_valid_input_string(param) for param in[nome, especialidade, crm]):
        return jsonify({"message": "Dados inválidos para a atualização de um médico!"}), 400
    try:
        medico = db.session.get(Medico, medico_id)
        if not medico:
            return jsonify({"message": f"Médico com ID {medico_id} não foi encontrado!"}), 404
        medico.nome = nome
        medico.especialidade = especialidade
        medico.crm = crm
        db.session.commit()
        return jsonify({"message": "Médico atualizado com sucesso!"}), 200
    except IntegrityError as integrity_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de integridade ao atualizar médico: {str(integrity_error)}"}), 409
    except SQLAlchemyError as sqlalchemy_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de banco de dados ao atualizar médico: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        db.session.rollback()
        return jsonify({"message": f"Erro inesperado ao atualizar médico: {str(exception)}"}), 500

def delete_medico(medico_id):
    if not medico_id:
        return jsonify({"message": f"Informe o ID do médico!"}), 400
    try:
        medico = db.session.get(Medico, medico_id)
        if not medico:
            return jsonify({"message": f"Médico com ID {medico_id} não foi encontrado!"}), 404
        consultas_associadas = db.session.query(Consulta).filter_by(medico_id=medico_id).count()
        if consultas_associadas > 0:
            return jsonify({"message": f"O médico {medico.nome} já está em {consultas_associadas} consulta(s) e não pode ser deletado."}), 409
        db.session.delete(medico)
        db.session.commit()
        return jsonify({"message": "Médico excluído com sucesso!"}), 200
    except SQLAlchemyError as sqlalchemy_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de banco de dados ao deletar médico: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        db.session.rollback()
        return jsonify({"message": f"Erro inesperado ao deletar médico: {str(exception)}"}), 500
