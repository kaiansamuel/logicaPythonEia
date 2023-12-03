class aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
    def matricular(self):
        print('Aluno ', self.nome, 'esta matriculado')

jose = aluno('123', 'José da Silva')
print(jose)
jose.matricular()
