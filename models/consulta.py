from extensions import db

class Consulta(db.Model):
    __tablename__ = 'consultas'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String, nullable=False)
    horario = db.Column(db.String(10), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    
    def __init__(self, data, horario, descricao, paciente_id, medico_id):
        self.data = data
        self.horario = horario
        self.descricao = descricao
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        
    def __repr__(self):
        return f'<Consulta {self.data}>'
    
    def to_dict(self):
        return {
            'id' : self.id,
            'data' : self.data,
            'horario' : self.horario,
            'descricao' : self.descricao,
            'paciente_id' : self.paciente_id,
            'medico_id' : self.medico_id
        }
        
        
    