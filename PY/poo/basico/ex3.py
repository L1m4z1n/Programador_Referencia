#Livro
#Crie uma classe Livro com atributos como título, autor, ano de publicação e páginas.
#Funcionalidades: Adicione um método para exibir as informações do livro e outro para calcular quantas páginas faltam para terminar o livro, dado o número de páginas lidas.

class Livro:
    def __init__(self, titulo, autor,ano_publicacao, paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.paginas = paginas

    def info(self):
        print(f"Titulo: {self.titulo}\nAutor: {self.autor}\nAno da Publicação: {self.ano_publicacao}\nPáginas: {self.paginas}")

    def paginas_lidas(self,paginas_lidas):
        self.paginas_lidas = paginas_lidas
        faltam = self.paginas-self.paginas_lidas
        print(f"O livro possui {self.paginas} páginas, {self.paginas_lidas} páginas já foram lidas e faltam {faltam}!")

livro = Livro("BioLima","Liminha",2025,100)
livro.info()

livro.paginas_lidas(60)
