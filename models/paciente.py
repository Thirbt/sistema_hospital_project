from extensions import db

class Paciente(db.Model):
    __tablename__='pacientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    
    consultas = db.relationship('Consulta', backref='paciente', lazy=True)
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return f'<Paciente {self.nome}>'
    
    def to_dict(self):
        return {
           'id' : self.id,
           'nome' : self.nome,
           'idade' : self.idade 
        }