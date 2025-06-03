from controllers.medico import medico_bp

from config import app,db
from flask_cors import CORS

CORS(app, origins=["http://127.0.0.1:0000"])

db.init_app(app)    

with app.app_context():
    db.create_all()

app.register_blueprint(medico_bp)


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
