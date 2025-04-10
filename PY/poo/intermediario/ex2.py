#Cadastro de Produtos
#Crie uma classe Produto com atributos como nome, preço e quantidade em estoque.
#Funcionalidades: Adicione métodos para atualizar a quantidade, aplicar descontos e calcular o valor total em estoque.

class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco= preco
        self.quantidade= quantidade

    def get_preco(self):
        return self.preco
    
    def set_preco(self, desconto):
        self.preco= self.preco-(self.preco*desconto/100)
        print(f"{self.preco}")

    def get_quant(self):
        return self.quantidade
    
    def set_quant(self,atualizar):
        self.quantidade+=atualizar
        print(f"{self.quantidade} Produtos")

    def total(self):
        total = self.quantidade*self.preco
        return total   
    

p= Produto("Vassoura",30,20)
print(f"Preço da {p.nome}: {p.get_preco()}")
descont = int(input("Quanto de desconto(%):"))
p.set_preco(descont)
print(f"Quantidade atual: {p.get_quant()}")
new_product=int(input("Adicionar Produto:"))
p.set_quant(new_product)
print(f"Valor total de Estoque: {p.total()}")