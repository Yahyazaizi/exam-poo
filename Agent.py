from Employe1 import Employe

class Agent(Employe):
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase, primeRespo):
        super().__init__(mtle, nom, dateNaissance, dateEmbuche, salaireBase)
        self.primeRespo = primeRespo

    def salaireAPayer(self):
        salaireNet = (self.salaireBase + self.primeRespo) * (1 - self.geIR(self.salaireBase))
        return salaireNet 