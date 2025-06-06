from flask import Blueprint, request, jsonify
from repositories.consulta import create_consulta, get_consulta, get_consulta_by_id, update_consulta, delete_consulta

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consultas')

@consulta_bp.route('', methods=['POST'])
def add_consulta():
    data = request.get_json()
    create_consulta(data['data'], data['horario'], data['descricao'])
    
    
@consulta_bp.route('', methods=['GET'])
def get_all_consultas():
    consultas = get_consulta()
    return jsonify([consulta.to_dict() for consulta in consultas])

@consulta_bp.route('', methods=['GET'])
def get_consulta(id):
    consulta = get_consulta_by_id(id)
    if consulta:
        return jsonify(consulta.to_dict())
    return jsonify({"message": "Consulta não encontrada!"}), 404

@consulta_bp.route('', methods=['PUT'])
def update_consulta_route(id):
    data = request.get_json()
    update_consulta(id, data.get('data'), data.get('horario'), data.get('descricao'))
    return jsonify({"message": "Consulta atualizada com sucesso!"})

@consulta_bp.route('', methods=['DELETE'])
def delete_consulta_route(id):
    delete_consulta(id)
    return jsonify({"message": "Consulta deltada com sucesso!"})
    