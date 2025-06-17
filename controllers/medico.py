# controllers/medico.py

from flask import Blueprint, request
from repositories.medico import create_medico, get_medicos, get_medico_by_id, update_medico, delete_medico

medico_bp = Blueprint('medico_bp', __name__, url_prefix='/medicos')

@medico_bp.route('/create', methods=["POST"])
def add_medico():
    """
    Cria um novo médico no sistema.
    ---
    parameters:
      - in: body
        name: medico
        schema:
          type: object
          required:
            - nome
            - especialidade
            - crm
          properties:
            nome:
              type: string
              description: "Nome completo do médico."
              example: "Dr. Carlos Eduardo"
            especialidade:
              type: string
              description: "Especialidade do médico."
              example: "Cardiologia"
            crm:
              type: string
              description: "Número de registro no CRM (deve ser único)."
              example: "SP123456"
    responses:
      201:
        description: "Médico criado com sucesso."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Médico Dr. Carlos Eduardo foi criado com sucesso!"
      400:
        description: "Dados inválidos fornecidos."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Dados inválidos para a criação de um médico!"
      409:
        description: "Erro de integridade de dados (ex: CRM duplicado)."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de integridade ao criar médico: [detalhes do erro]"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao criar médico: [detalhes do erro]"
    tags:
      - Médicos
    """
    data = request.get_json()
    return create_medico(data.get("nome"), data.get("especialidade"), data.get("crm"))

@medico_bp.route('/findAll', methods=["GET"])
def get_all_medicos():
    """
    Lista todos os médicos registrados.
    ---
    responses:
      200:
        description: "Lista de médicos."
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              nome:
                type: string
                example: "Dr. Carlos Eduardo"
              especialidade:
                type: string
                example: "Cardiologia"
              crm:
                type: string
                example: "SP123456"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de banco de dados ao buscar médicos: [detalhes do erro]"
    tags:
      - Médicos
    """
    return get_medicos()

@medico_bp.route('/findById/<int:id>', methods=["GET"])
def get_medico(id):
    """
    Busca um médico específico pelo seu ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "O ID único do médico a ser buscado."
        example: 1
    responses:
      200:
        description: "Detalhes do médico encontrado."
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nome:
              type: string
              example: "Dr. Carlos Eduardo"
            especialidade:
              type: string
              example: "Cardiologia"
            crm:
              type: string
              example: "SP123456"
      400:
        description: "ID do médico não fornecido."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Informe o ID do médico!"
      404:
        description: "Médico não encontrado."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Médico com ID 99 não foi encontrado!"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao buscar médico: [detalhes do erro]"
    tags:
      - Médicos
    """
    return get_medico_by_id(id)

@medico_bp.route('/update/<int:id>', methods=["PUT"])
def update_medico_route(id):
    """
    Atualiza as informações de um médico existente.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "O ID do médico a ser atualizado."
        example: 1
      - in: body
        name: medico
        schema:
          type: object
          required:
            - nome
            - especialidade
            - crm
          properties:
            nome:
              type: string
              description: "Novo nome completo do médico."
              example: "Dr. Carlos Almeida"
            especialidade:
              type: string
              description: "Nova especialidade do médico."
              example: "Dermatologia"
            crm:
              type: string
              description: "Novo número de registro no CRM (deve ser único)."
              example: "SP654321"
    responses:
      200:
        description: "Médico atualizado com sucesso."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Médico atualizado com sucesso!"
      400:
        description: "Dados inválidos fornecidos para a atualização."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Dados inválidos para a atualização de um médico!"
      404:
        description: "Médico não encontrado."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Médico com ID 99 não foi encontrado!"
      409:
        description: "Erro de integridade de dados (ex: CRM duplicado)."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de integridade ao atualizar médico: [detalhes do erro]"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao atualizar médico: [detalhes do erro]"
    tags:
      - Médicos
    """
    data = request.get_json()
    return update_medico(id, data.get("nome"), data.get("especialidade"), data.get("crm"))

@medico_bp.route('/delete/<int:id>', methods=["DELETE"])
def delete_medico_route(id):
    """
    Deleta um médico do sistema pelo seu ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "O ID do médico a ser deletado."
        example: 1
    responses:
      200:
        description: "Médico excluído com sucesso."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Médico excluído com sucesso!"
      400:
        description: "ID do médico não fornecido."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Informe o ID do médico!"
      404:
        description: "Médico não encontrado."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Médico com ID 99 não foi encontrado!"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao excluir médico: [detalhes do erro]"
    tags:
      - Médicos
    """
    return delete_medico(id)