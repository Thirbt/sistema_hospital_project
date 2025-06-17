from models.paciente import Paciente
from extensions import db
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from utilities.utility import is_valid_input_string

def create_paciente(nome, idade):
    if not is_valid_input_string(nome):
        return jsonify({"message": "Dados inválidos para a criação de um paciente! O nome é obrigatório e não pode ser vazio."}), 400
    
    if not isinstance(idade, int) or idade <= 0:
        return jsonify({"message": "Dados inválidos para a criação de um paciente! A idade deve ser um número inteiro positivo."}), 400
    
    try:
        paciente = Paciente(nome = nome, idade = idade)
        db.session.add(paciente)
        db.session.commit()
        return jsonify({"message": f"Paciente {nome} foi criado com sucesso!"}), 201
    except IntegrityError as integrity_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de integridade ao criar paciente: {str(integrity_error)}"}), 409
    except SQLAlchemyError as sqlalchemy_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de banco de dados ao criar paciente: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        db.session.rollback()
        return jsonify({"message": f"Erro inesperado ao criar paciente: {str(exception)}"}), 500
    
def get_pacientes():
    try:
        pacientes = Paciente.query.all()
        return jsonify([paciente.to_dict() for paciente in pacientes]), 200
    except SQLAlchemyError as sqlalchemy_error:
        return jsonify({"message": f"Erro de banco de dados ao buscar pacientes: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        return jsonify({"message": f"Erro inesperado ao buscar pacientes: {str(exception)}"}), 500

def get_paciente_by_id(paciente_id):
    if not paciente_id:
        return jsonify({"message": "Informe o ID do paciente!"}), 400
    try:
        paciente = db.session.get(Paciente, paciente_id)
        if not paciente:
            return jsonify({"message": f"Paciente com ID {paciente_id} não foi encontrado!"}), 404
        return jsonify(paciente.to_dict()), 200
    except SQLAlchemyError as sqlalchemy_error:
        return jsonify({"message": f"Erro de banco de dados ao buscar paciente: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        return jsonify({"message": f"Erro inesperado ao buscar paciente: {str(exception)}"}), 500

def update_paciente(paciente_id, nome, idade):
    if not paciente_id:
        return jsonify({"message": "ID do paciente é obrigatório para a atualização!"}), 400

    if not is_valid_input_string(nome):
        return jsonify({"message": "Dados inválidos para a atualização de um paciente! O nome é obrigatório e não pode ser vazio."}), 400
    
    if not isinstance(idade, int) or idade <= 0:
        return jsonify({"message": "Dados inválidos para a atualização de um paciente! A idade deve ser um número inteiro positivo."}), 400
    
    try:
        paciente = db.session.get(Paciente, paciente_id)
        if not paciente:   
            return jsonify({"message": f"Paciente com ID {paciente_id} não foi encontrado!"}), 404
        paciente.nome = nome
        paciente.idade = idade
        db.session.commit()
        return jsonify({"message": "Paciente atualizado com sucesso!"}), 200
    except IntegrityError as integrity_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de integridade ao atualizar paciente: {str(integrity_error)}"}), 409
    except SQLAlchemyError as sqlalchemy_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de banco de dados ao atualizar paciente: {str(sqlalchemy_error)}"}), 500
    except Exception as exception:
        db.session.rollback()
        return jsonify({"message": f"Erro inesperado ao atualizar paciente: {str(exception)}"}), 500

def delete_paciente(paciente_id):
    if not paciente_id:
        return jsonify({"message": "Informe o ID do paciente!"}), 400 
    try:
        paciente = db.session.get(Paciente, paciente_id)
        if not paciente:
            return jsonify({"message": f"Paciente com ID {paciente_id} não foi encontrado!"}), 404
        db.session.delete(paciente)
        db.session.commit()
        return jsonify({"message": "Paciente excluído com sucesso!"}), 200
    except SQLAlchemyError as sqlachemy_error:
        db.session.rollback()
        return jsonify({"message": f"Erro de banco de dados ao excluir paciente: {str(sqlachemy_error)}"}), 500
    except Exception as exception:
        db.session.rollback()
        return jsonify({"message": f"Erro inesperado ao excluir paciente: {str(exception)}"}), 500