from config import db

class Consulta(db.Model):
    __tablename__ = 'consultas'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    horario = db.Column(db.String(10), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    
    def __init__(self, data, horario, descricao):
        self.data = data
        self.horario = horario
        self.descricao = descricao
        
    def __repr__(self):
        return f'<Consulta {self.data}>'
    
    def to_dict(self):
        return {
            'id' : self.id,
            'data' : self.data,
            'horario' : self.horario,
            'descricao' : self.descricao
        }
        
        
    