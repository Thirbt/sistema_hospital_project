class PacienteDTO():
    def __init__(self, paciente):
        self.id = paciente.id
        self.nome = paciente.nome
        self.idade = paciente.idade
        
    def to_dict(self):
        return {
           'id' : self.id,
           'nome' : self.nome,
           'idade' : self.idade 
        }