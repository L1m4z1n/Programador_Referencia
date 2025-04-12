class Preferencial:
    def __init__(self):
        self.filapreferencial = []

    def adicionar(self,paciente):
        self.filapreferencial.append(paciente)

    def atender_pref(self):
        if self.filapreferencial:
            return self.filapreferencial.pop(0)
        else:
            return None
        
class Normal:
    def __init__(self):
        self.filanormal = []

    def adicionar(self,paciente):
        self.filanormal.append(paciente)

    def atender_pref(self):
        if self.filanormal:
            return self.filanormal.pop(0)
        else:
            return None
        
class Atendimento:
    def __init__(self):
        self.filapreferencial = Preferencial()
        self.filanormal = Normal()

    def adc_paciente(self,nome,tipo):
        if tipo == "Preferencial":
            self.filapreferencial.adicionar(nome)
        elif tipo == "Normal":
            self.filanormal.adicionar(nome)
        else:
            print("Normal ou Preferencial!")    

    def atender_paciente(self):
        if self.fila_preferencial.filapreferencial:
            paciente=self.filapreferencial.atender()
            print(f"Atendendo paciente preferencial: {paciente}")
        elif self.fila_normal.filanormal:
            paciente=self.filanormal.atender()
            print(f"Atendendo paciente normal: {paciente}")
        else:
            print("Nenhum paciente!")

atendimento = Atendimento()
while True:
    print("\nMenu:")
    print("1 - Adicionar Paciente")
    print("2 - Atender Paciente")
    print("3 - Sair")
    opcao=int(input("Escolha uma opção: "))

    if opcao == 1:
        nome=input("Digite o nome do paciente:")
        tipo=input("Atendimento 'Normal' ou 'Preferencial': ")
        atendimento.adc_paciente(nome,tipo)
    elif opcao == 2:
        atendimento.atender_paciente()
    elif opcao == 3:
        print("Encerrando o atendimento...")
    break
else:
    print("Opção invalida")
        