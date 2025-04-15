#Nível Avançado (POO)
#Sistema de Biblioteca Avançado
#Crie uma classe Livro e uma classe Cliente para um sistema de biblioteca.
#Funcionalidades: O Cliente pode emprestar e devolver livros. O Livro pode ter informações como título, autor, status (disponível ou emprestado). Implemente herança para diferentes tipos de livros e métodos polimórficos para gerenciar a devolução.

class Livro:
    def __init__(self,titulo,autor,status="Disponivel"):
        self.titulo=titulo
        self.autor=autor
        self.status=status

    def emprestar(self):
        if self.status == "Disponivel":
            self.status = "Emprestado"
            return True
        return False
    
    def devolver(self):
       if self.status == "Emprestado":
            self.status = "Disponivel"
            return True
       return False 

class LivroFisico(Livro):
    def devolver(self):
       if self.status == "Emprestado":
            self.status = "Disponivel"
            print(f"O livro fisico '{self.titulo}' foi devolvido ao balcão da biblioteca!")
            return True
       return False 

class LivroDigital(Livro):
    def devolver(self):
       if self.status == "Emprestado":
            self.status = "Disponivel"
            print(f"O livro digital '{self.titulo}' foi devolvido ao balcão da biblioteca!")
            return True
       return False 
    
class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.livros_emprestados = []

    def emprestar_livro(self,livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print(f"{self.nome} emprestou o {livro.titulo}")
        else:
            print(f"'{livro.titulo}' está disponivel!")

    def devolver_livro(self,livro):
        if livro.devolver():
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu '{livro.titulo}'")
        else:
            print(f"{livro.titulo} está disponivel!")

livros = [
    LivroFisico("Dom Quixote", "Miguel de Cervantes"),
    LivroDigital("1984", "George Orwell"),
    LivroFisico("O Senhor dos Anéis", "J.R.R. Tolkien")
]
cliente = Cliente("Gabriel")

while True:
    print("\n===== Biblioteca Interativa =====")
    print("1. Listar Livros")
    print("2. Emprestar Livro")
    print("3. Devolver Livro")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        print("\nLista de Livros:")
        for i, livro in enumerate(livros):
            print(f"{i + 1}. {livro.titulo} ({livro.autor}) - {livro.status}")

    elif escolha == "2":
        num = int(input("Digite o número do livro para emprestar: ")) - 1
        if 0 <= num < len(livros):
            cliente.emprestar_livro(livros[num])
        else:
            print("Número inválido.")

    elif escolha == "3":
        num = int(input("Digite o número do livro para devolver: ")) - 1
        if 0 <= num < len(livros):
            cliente.devolver_livro(livros[num])
        else:
            print("Número inválido.")

    elif escolha == "4":
        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida. Tente novamente!")
