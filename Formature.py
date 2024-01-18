from IEmploye import IEmploye
class Formature(IEmploye):
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase, heurSup):
        super().__init__(mtle, nom, dateNaissance, dateEmbuche, salaireBase)
        self.heurSup = heurSup
        self.tariSup = 70

    @property
    def heurSup(self):
        return self.heurSup
    @heurSup.setter
    def heurSup(self,h):
        self.heurSup = h

    @property
    def tarifSup(self):
        return self.tarifSup

    def __str__(self):
        return f"{self.__str__()} - {self.heurSup} - {self.tarifSup}"

    def salaireAPayer(self):
        salaireNet = (self.salaireBase + self.heurSup * self.tarifSup ) * (1-self.geIR(self.salaireBase))
        return salaireNet