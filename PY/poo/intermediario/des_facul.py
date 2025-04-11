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
        