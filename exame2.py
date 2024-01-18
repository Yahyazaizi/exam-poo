class IR:
    def __init__(self):
        self.tranches = [0,30000, 50000, 60000, 80000, 180000]
        self.tauxIR = [0,10, 20, 30, 34, 38]

    def geIR(self,salaire):
        salaireAnnuel = salaire * 12
        for i in range(5,-1,-1):
            if salaireAnnuel > self.tranches[i]:
                return  self.tauxIR[i] / 100




                       