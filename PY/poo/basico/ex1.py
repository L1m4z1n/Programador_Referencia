#Nível Básico (POO)
#Cadastro de Pessoa
#Crie uma classe Pessoa com atributos como nome, idade e endereço.
#Funcionalidades: Defina métodos para exibir as informações de uma pessoa e atualizar a idade.

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def info(self):
        print(f"Nome: {self.nome}")    
        print(f"Idade: {self.idade}")    
        print(f"Endereço: {self.endereco}")    

    def atualizar_idade(self,nova_idade):
        self.idade = nova_idade
        print(f"Nova Idade: {self.idade}")

pessoa = Pessoa("Gabriel Lima",18,"Brasilia-DF")    
pessoa.info()

pessoa.atualizar_idade(19)
pessoa.info()