# controllers/consulta.py

from flask import Blueprint, request
from repositories.consulta import create_consulta, get_consulta, get_consulta_by_id, update_consulta, delete_consulta

consulta_bp = Blueprint('consulta_bp', __name__, url_prefix='/consultas')

@consulta_bp.route('/create', methods=["POST"])
def add_consulta():
    """
    Cria uma nova consulta médica.
    ---
    parameters:
      - in: body
        name: consulta
        schema:
          type: object
          required:
            - data
            - horario
            - descricao
            - paciente_id
            - medico_id
          properties:
            data:
              type: string
              format: dd/mm/YYYY
              description: "Data da consulta no formato dd/mm/YYYY."
              example: "16/06/2025"
            horario:
              type: string
              description: "Horário da consulta (ex: '14:30')."
              example: "14:30"
            descricao:
              type: string
              description: "Breve descrição ou motivo da consulta."
              example: "Dor de cabeça e febre"
            paciente_id:
              type: integer
              description: "ID do paciente associado à consulta."
              example: 1
            medico_id:
              type: integer
              description: "ID do médico associado à consulta."
              example: 1
    responses:
      201:
        description: "Consulta criada com sucesso."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Consulta criada com sucesso!"
            consulta_id:
              type: integer
              example: 1
      400:
        description: "Dados inválidos ou formato de data incorreto (use 'dd/mm/YYYY')."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Formato de data inválido. Use 'dd/mm/YYYY' como string."
      404:
        description: "Paciente ou médico não encontrado."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "O paciente com ID 99 não foi encontrado!"
      409:
        description: "Erro de integridade de dados (ex: se houvesse restrições únicas)."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de integridade ao criar consulta: [detalhes do erro]"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao criar consulta: [detalhes do erro]"
    tags:
      - Consultas
    """
    data = request.get_json()
    return create_consulta(data.get("data"), data.get("horario"), data.get("descricao"), data.get("paciente_id"), data.get("medico_id"))

@consulta_bp.route('/findAll', methods=["GET"])
def get_all_consultas():
    """
    Lista todas as consultas médicas registradas.
    ---
    responses:
      200:
        description: "Lista de consultas."
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              data:
                type: string
                format: dd/mm/YYYY
                example: "16/06/2025"
              horario:
                type: string
                example: "14:30"
              descricao:
                type: string
                example: "Dor de cabeça"
              paciente_id:
                type: integer
                example: 1
              medico_id:
                type: integer
                example: 1
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de banco de dados ao buscar consultas: [detalhes do erro]"
    tags:
      - Consultas
    """
    return get_consulta()

@consulta_bp.route('/findById/<int:id>', methods=["GET"])
def get_single_consulta(id):
    """
    Busca uma consulta médica específica pelo seu ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "O ID único da consulta a ser buscada."
        example: 1
    responses:
      200:
        description: "Detalhes da consulta encontrada."
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            data:
              type: string
              format: dd/mm/YYYY
              example: "16/06/2025"
            horario:
              type: string
              example: "14:30"
            descricao:
              type: string
              example: "Dor de cabeça"
            paciente_id:
              type: integer
              example: 1
            medico_id:
              type: integer
              example: 1
      400:
        description: "ID da consulta não fornecido."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Informe o ID da consulta!"
      404:
        description: "Consulta não encontrada."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "A consulta com ID 99 não foi encontrada!"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao buscar consulta: [detalhes do erro]"
    tags:
      - Consultas
    """
    return get_consulta_by_id(id)

@consulta_bp.route('/update/<int:id>', methods=["PUT"])
def update_consulta_route(id):
    """
    Atualiza as informações de uma consulta médica existente.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "O ID da consulta a ser atualizada."
        example: 1
      - in: body
        name: consulta
        schema:
          type: object
          required:
            - data
            - horario
            - descricao
            - paciente_id
            - medico_id
          properties:
            data:
              type: string
              format: dd/mm/YYYY
              description: "Nova data da consulta no formato dd/mm/YYYY."
              example: "17/06/2025"
            horario:
              type: string
              description: "Novo horário da consulta (ex: '15:00')."
              example: "15:00"
            descricao:
              type: string
              description: "Nova descrição ou motivo da consulta."
              example: "Retorno médico"
            paciente_id:
              type: integer
              description: "Novo ID do paciente associado à consulta."
              example: 2
            medico_id:
              type: integer
              description: "Novo ID do médico associado à consulta."
              example: 2
    responses:
      200:
        description: "Consulta atualizada com sucesso."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Consulta atualizada com sucesso!"
      400:
        description: "Dados inválidos ou formato de data incorreto (use 'dd/mm/YYYY')."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Formato de data inválido para atualização. Use 'dd/mm/YYYY' como string."
      404:
        description: "Consulta, paciente ou médico não encontrado."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "A consulta com ID 99 não foi encontrada!"
      409:
        description: "Erro de integridade de dados (ex: se houvesse restrições únicas)."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de integridade ao atualizar consulta: [detalhes do erro]"
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao atualizar consulta: [detalhes do erro]"
    tags:
      - Consultas
    """
    data = request.get_json()
    return update_consulta(
        id,
        data.get("data"),
        data.get("horario"),
        data.get("descricao"),
        data.get("paciente_id"),
        data.get("medico_id")
    )

@consulta_bp.route('/delete/<int:id>', methods=["DELETE"])
def delete_consulta_route(id):
    """
    Deleta uma consulta médica pelo seu ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "O ID da consulta a ser deletada."
        example: 1
    responses:
      200:
        description: "Consulta deletada com sucesso."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Consulta deletada com sucesso!"
      400:
        description: "ID da consulta não fornecido."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Informe o ID da consulta!"
      404:
        description: "Consulta não encontrada."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "A consulta com ID 99 não foi encontrada!"
      409:
        description: "Erro de integridade de dados (ex: se houver dependências que impeçam a deleção)."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro de integridade ao deletar consulta: Existem referências a ela."
      500:
        description: "Erro interno do servidor ou de banco de dados."
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Erro inesperado ao deletar consulta: [detalhes do erro]"
    tags:
      - Consultas
    """
    # A linha está truncada, mas o essencial é o docstring
    return delete_consulta(id)