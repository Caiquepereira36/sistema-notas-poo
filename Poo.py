class Aluno:

    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
        
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6:
            return 'Aluno Aprovado'
        else:
            return 'Aluno Reprovado'
        
for alunos in range(3):
    nome = input(f'Digite o nome do aluno {alunos + 1}: ')
    notas = []
    for j in range(3):
        nota = float(input(f'Digite a nota {j + 1} do aluno {nome}:'))
        notas.append(nota)
    aluno = Aluno(nome, notas)
    media = aluno.calcular_media()
    situacao = aluno.verificar_aprovacao()

    print(f'\nAluno: {aluno.nome}')
    print(f'Notas: {aluno.notas}')
    print(f'Média: {media:.2f}')
    print(f'Situação: {situacao}\n')