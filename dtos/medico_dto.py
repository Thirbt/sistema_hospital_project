class MedicoDTO:
    def __init__(self, medico):
        self.id = medico.id
        self.nome = medico.nome
        self.especialidade = medico.especialidade
        self.crm = medico.crm
        
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'especialidade': self.especialidade,
            'crm': self.crm
        }
        
        
    