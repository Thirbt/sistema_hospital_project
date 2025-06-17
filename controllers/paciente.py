# controllers/paciente.py

from flask import Blueprint, request
from repositories.paciente import create_paciente, get_pacientes, get_paciente_by_id, update_paciente, delete_paciente

paciente_bp = Blueprint('paciente_bp', __name__, url_prefix='/pacientes')

@paciente_bp.route('/create', methods=["POST"])
def add_paciente():
    """
    Cria um novo paciente no sistema.
    ---
    parameters:
      - in: body
        name: paciente
        schema:
          type: object
          required:
            - nome
            - idade
          properties:
            nome:
              type: string
              description: "Nome completo do paciente."
              example: "Ana Costa"
            idade:
              type: integer
              description: "Idade do paciente em anos."
              example: 28
    responses:
      201:
        description: "Paciente criado com sucesso."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Paciente Ana Costa foi criado com sucesso!"
      400:
        description: "Dados inválidos fornecidos."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Dados inválidos para a criação de um paciente!"
      409:
        description: "Erro de integridade de dados (ex: CRM duplicado, se fosse o caso, ou outra restrição)."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de integridade ao criar paciente: [detalhes do erro]"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao criar paciente: [detalhes do erro]"
    tags:
      - Pacientes
    """
    data = request.get_json()
    return create_paciente(data.get("nome"), data.get("idade"))

@paciente_bp.route('/findAll', methods=["GET"])
def get_all_pacientes():
    """
    Lista todos os pacientes registrados.
    ---
    responses:
      200:
        description: "Lista de pacientes."
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: "ID único do paciente."
                example: 1
              nome:
                type: string
                description: "Nome completo do paciente."
                example: "Ana Costa"
              idade:
                type: integer
                description: "Idade do paciente."
                example: 28
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de banco de dados ao buscar pacientes: [detalhes do erro]"
    tags:
      - Pacientes
    """
    return get_pacientes()

@paciente_bp.route('/findById/<int:id>', methods=["GET"])
def get_paciente(id):
    """
    Busca um paciente específico pelo seu ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "O ID único do paciente a ser buscado."
        example: 1
    responses:
      200:
        description: "Detalhes do paciente encontrado."
        schema:
          type: object
          properties:
            id:
              type: integer
              description: "ID único do paciente."
              example: 1
            nome:
              type: string
              description: "Nome completo do paciente."
              example: "Ana Costa"
            idade:
              type: integer
              description: "Idade do paciente."
              example: 28
      400:
        description: "ID do paciente não fornecido."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Informe o ID do paciente!"
      404:
        description: "Paciente não encontrado."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Paciente com ID 99 não foi encontrado!"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao buscar paciente: [detalhes do erro]"
    tags:
      - Pacientes
    """
    return get_paciente_by_id(id)

@paciente_bp.route('/update/<int:id>', methods=["PUT"])
def update_paciente_route(id):
    """
    Atualiza as informações de um paciente existente.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "O ID do paciente a ser atualizado."
        example: 1
      - in: body
        name: paciente
        schema:
          type: object
          required:
            - nome
            - idade
          properties:
            nome:
              type: string
              description: "Novo nome do paciente."
              example: "Ana Maria"
            idade:
              type: integer
              description: "Nova idade do paciente."
              example: 29
    responses:
      200:
        description: "Paciente atualizado com sucesso."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Paciente atualizado com sucesso!"
      400:
        description: "Dados inválidos fornecidos para a atualização."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Dados inválidos para a atualização de um paciente!"
      404:
        description: "Paciente não encontrado."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Paciente com ID 99 não foi encontrado!"
      409:
        description: "Erro de integridade de dados (ex: CRM duplicado, se fosse o caso, ou outra restrição)."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de integridade ao atualizar paciente: [detalhes do erro]"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao atualizar paciente: [detalhes do erro]"
    tags:
      - Pacientes
    """
    data = request.get_json()
    return update_paciente(id, data.get("nome"), data.get("idade"))

@paciente_bp.route('/delete/<int:id>', methods=["DELETE"])
def delete_paciente_route(id):
    """
    Deleta um paciente do sistema pelo seu ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "O ID do paciente a ser deletado."
        example: 1
    responses:
      200:
        description: "Paciente excluído com sucesso."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Paciente excluído com sucesso!"
      400:
        description: "ID do paciente não fornecido."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Informe o ID do paciente!"
      404:
        description: "Paciente não encontrado."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Paciente com ID 99 não foi encontrado!"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao excluir paciente: [detalhes do erro]"
    tags:
      - Pacientes
    """
    return delete_paciente(id)