from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger

db = SQLAlchemy()
cors = CORS()
swagger = Swagger()