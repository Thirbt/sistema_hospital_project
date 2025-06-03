from flask import Blueprint, request, jsonify
from repositories.medico import create_medico, get_medicos, get_medico_by_id, update_medico, delete_medico

medico_bp = Blueprint('medico', __name__, url_prefix='/medicos')

@medico_bp.route('', methods=['POST'])
def add_medico():
    data = request.get_json()
    create_medico(data['nome'], data['especialidade'], data['crm'])
    return jsonify({"message": "Médico criado com sucesso!"}), 201

@medico_bp.route('', methods=['GET'])
def get_all_medicos():
    medicos = get_medicos()
    return jsonify([medico.to_dict() for medico in medicos])

# Rota para obter um médico por ID
@medico_bp.route('/<int:id>', methods=['GET'])
def get_medico(id):
    medico = get_medico_by_id(id)
    if medico:
        return jsonify(medico.to_dict())
    return jsonify({"message": "Médico não encontrado!"}), 404

# Rota para atualizar um médico
@medico_bp.route('/<int:id>', methods=['PUT'])
def update_medico_route(id):
    data = request.get_json()
    update_medico(id, data.get('nome'), data.get('especialidade'), data.get('crm'))
    return jsonify({"message": "Médico atualizado com sucesso!"})

# Rota para excluir um médico
@medico_bp.route('/<int:id>', methods=['DELETE'])
def delete_medico_route(id):
    delete_medico(id)
    return jsonify({"message": "Médico deletado com sucesso!"})
