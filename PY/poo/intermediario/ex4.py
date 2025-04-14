#Sistema de Alunos
#Crie uma classe Aluno com atributos como nome, matrícula e notas.
#Funcionalidades: Implemente métodos para calcular a média das notas e verificar se o aluno foi aprovado ou reprovado.

class Aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula= matricula
        self.media = 0
        
    def calc_media(self,nota1,nota2):
        self.media=(nota1+nota2)/2

    def resul(self):
        if self.media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

nome=str(input("Nome do Aluno: "))
matricula=str(input("Materia: "))
aluno=Aluno(nome,matricula)

nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))

aluno.calc_media(nota1,nota2)
print(f"Primeira nota: {nota1}\nSegunda nota: {nota2}\nMédia: {aluno.media}\nResultado: {aluno.resul()}")

