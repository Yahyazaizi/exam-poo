import json
form EmployeFile import Employe
class Formature(Employe):
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
   
    def addFormateurToJSON(self):
        with open("foramteurs.json","r") as file:
            data = json.load(file)
        newForm = {"matricule": self.mtle, 
                   "nom": self.nom, 
                   "date naissance": self.dateNaissance, 
                   "date embuche": self.dateEmbuche,
                   "salaire base": self.salaireBase,
                   "heur sup": self.heurSup}
        data.append(newForm)
        with open("foramteurs.json","w") as f:
            json.dump(data,f)
    def deleteForamteurFromJSON(self,FormteurID):
        with open("foramteurs.json","r") as file:
            data = json.load(file)
        
        for record in data:
            if record["matricule"] == FormteurID:
                del data[data.index(record)]
        with open("foramteurs.json","w") as f:
            json.dump(data,f)
    
    def findFormateurInJSON(self,FormateurID):
        with open("foramteurs.json","r") as file:
            data = json.load(file)
        
        for record in data:
            if record["matricule"] == FormateurID:
                return record
    
    def showAllFarmateur(self):
        with open("foramteurs.json","r") as file:
            data = json.load(file)
        return data


        
