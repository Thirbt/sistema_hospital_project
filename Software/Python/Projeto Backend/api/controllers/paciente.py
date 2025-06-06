from flask import Blueprint, request, jsonify
from repositories.paciente import create_paciente, get_pacientes, get_paciente_by_id, update_paciente, delete_paciente

paciente_bp = Blueprint('paciente', __name__, url_prefix='/pacientes')

@paciente_bp.route('', methods=['POST'])
def add_paciente():
    data = request.get_json()
    create_paciente(data['nome'], data['idade'])
    return jsonify({"message": "Paciente criado com sucesso!"}), 201

@paciente_bp.route('', methods=['GET'])
def get_all_pacientes():
    pacientes = get_pacientes()
    return jsonify([paciente.to_dict() for paciente in pacientes])

@paciente_bp.route('/<init:id>', methods=['GET'])
def get_paciente(id):
    paciente = get_paciente_by_id(id)
    if paciente:
        return jsonify(paciente.to_dict())
    return jsonify({"message": "Paciente não encontrado!"}), 404

@paciente_bp.route('/<int:id>', methods=['PUT'])
def update_paciente(id):
    data = request.get_json()
    update_paciente(id, data.get('nome'), data.get('idade'))
    return jsonify({"message": "Paciente atualizado com sucesso!"})

@paciente_bp.route('/<int:id>', methods=['DELETE'])
def delete_paciente(id):
    delete_paciente(id)
    return jsonify({"message": "Paciente deletado com sucesso!"})