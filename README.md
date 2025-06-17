# 🏥 Hospital API - Gerenciamento de Consultas Médicas

Bem-vindo à **Hospital API**, uma API RESTful desenvolvida em **Python** utilizando o framework **Flask** e **SQLAlchemy** para gerenciar informações de pacientes, médicos e consultas. Esta API foi construída com foco em **modularidade, robustez** e **tratamento abrangente de exceções**, garantindo uma comunicação clara e segura com o cliente.

## 🚀 Funcionalidades

Esta API permite o gerenciamento completo das seguintes entidades:

* **Pacientes:** Cadastro, listagem, busca por ID, atualização e exclusão.
* **Médicos:** Cadastro, listagem, busca por ID, atualização e exclusão.
* **Consultas:** Agendamento, listagem, busca por ID, atualização e exclusão, com validação de existência de médico e paciente.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Flask:** Microframework web para Python.
* **Flask-SQLAlchemy:** Extensão Flask para integração com SQLAlchemy (ORM).
* **SQLAlchemy:** Toolkit SQL e Mapeador Objeto-Relacional (ORM).
* **SQLite:** Banco de dados leve e integrado (para desenvolvimento).
* **Flasgger:** Geração automática de documentação Swagger/OpenAPI.
* **Flask-CORS:** Habilita o Cross-Origin Resource Sharing para a API.
* **`re` (módulo regex):** Para validação de formato de strings (ex: data `dd/mm/YYYY`).

## 📦 Estrutura do Projeto

A organização do projeto segue princípios de modularidade e separação de responsabilidades:

```
.
├── controllers/
│   ├── consulta.py
│   ├── medico.py
│   └── paciente.py
├── models/
│   ├── consulta.py
│   ├── medico.py
│   └── paciente.py
├── repositories/
│   ├── consulta.py
│   ├── medico.py
│   └── paciente.py
├── utilities/
│   └── utilities.py
└── app.py

``` 

* **`app.py`**: Ponto de entrada principal da aplicação. Contém a inicialização do Flask, todas as configurações (incluindo Flasgger), inicialização das extensões (SQLAlchemy, CORS, Flasgger) e registro dos Blueprints.
* **`controllers/`**: Contêm os Blueprints do Flask, responsáveis por definir as rotas da API, receber as requisições HTTP e chamar as funções apropriadas na camada de repositório. Hospedam as docstrings YAML para a documentação Swagger.
* **`repositories/`**: Contêm a lógica de negócio e as operações de CRUD (Create, Read, Update, Delete) para cada entidade, interagindo diretamente com o banco de dados. Realizam o tratamento abrangente de exceções e validação de dados de entrada, como a verificação de strings não vazias e o formato específico de datas (`dd/mm/YYYY`).
* **`models/`**: Definem os modelos ORM (Object-Relational Mapping) para cada entidade (Paciente, Médico, Consulta) usando Flask-SQLAlchemy. Representam as tabelas do banco de dados e suas relações.
* **`utilities/`**: Contém funções utilitárias reutilizáveis, como a validação de strings de entrada (`is_valid_input_string`) e a validação de formato de data (`is_valid_date_format`).

## ⚙️ Configuração e Execução

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SeuUsuario/teste_hospital.git](https://github.com/SeuUsuario/teste_hospital.git) # Substitua pelo seu link do GitHub
    cd teste_hospital
    ```
2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```
3.  **Instale as dependências:**
    Você pode criar um `requirements.txt` com `pip freeze > requirements.txt` se já tiver tudo instalado, ou instalar manualmente:
    ```bash
    pip install Flask Flask-SQLAlchemy Flasgger Flask-Cors
    ```

### Rodando a Aplicação

Para iniciar o servidor de desenvolvimento e criar o banco de dados (se ainda não existir):

```bash
python app.py
```

Você verá a aplicação iniciar, provavelmente na porta 8000 e no modo Debug: on (conforme configurado em app.py).

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on [http://0.0.0.0:8080](http://0.0.0.0:8080) (Press CTRL+C to quit)

## 📚 Documentação da API (Swagger UI)

A API é auto-documentada usando Flasgger, fornecendo uma interface interativa via Swagger UI.

Após iniciar a aplicação, acesse a documentação em seu navegador:

```
http://127.0.0.1:8080/apidocs/
```

Aqui você poderá ver todos os endpoints disponíveis, seus parâmetros, exemplos de requisição e resposta, e testar as chamadas diretamente do navegador.

## 📝 Validações Importantes

* Campos Obrigatórios: Todos os campos necessários para criação/atualização de entidades são validados para não serem None e não serem strings vazias (mesmo que contenham apenas espaços em branco).

* Formato de Data: O campo data das consultas é validado para seguir estritamente o formato dd/mm/YYYY.

* Chaves Estrangeiras: Ao criar ou atualizar uma consulta, o sistema verifica se os IDs de paciente e médico fornecidos realmente existem no banco de dados, retornando 404 Not Found caso contrário.

* Unicidade: O campo crm do médico é validado como único. Tentar cadastrar ou atualizar um médico com um CRM já existente resultará em um erro 409 Conflict.