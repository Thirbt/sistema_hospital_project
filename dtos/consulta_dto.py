from dtos.medico_dto import MedicoDTO
from dtos.paciente_dto import PacienteDTO

class ConsultaDTO:
    def __init__(self, consulta):
        self.id = consulta.id
        self.data = consulta.data
        self.horario = consulta.horario
        self.descricao = consulta.descricao
        self.paciente = PacienteDTO(consulta.paciente).to_dict() if consulta.paciente else None
        self.medico = MedicoDTO(consulta.medico).to_dict() if consulta.medico else None
        
    def __repr__(self):
        return f'<Consulta {self.data}'
    
    def to_dict(self):
        return {
            'id' : self.id,
            'data' : self.data,
            'horario' : self.horario,
            'descricao' : self.descricao,
            'medico' : self.medico,
            'paciente' : self.paciente
        }