
form EmployeFile import Employe
class Agent(Employe):
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase, primeRespo):
        super().__init__(mtle, nom, dateNaissance, dateEmbuche, salaireBase)
        self.primeRespo = primeRespo

    def salaireAPayer(self):
        salaireNet = (self.salaireBase + self.primeRespo) * (1 - self.geIR(self.salaireBase))
        return salaireNet
     def addAgentToJSON(self):
        with open("agents.json","r") as file:
            data = json.load(file)
        newForm = {"matricule": self.mtle, 
                   "nom": self.nom, 
                   "date naissance": self.dateNaissance, 
                   "date embuche": self.dateEmbuche,
                   "salaire base": self.salaireBase,
                   "heur sup": self.primeRespo}
        data.append(newForm)
        with open("agents.json","w") as f:
            json.dump(data,f)
    

    def deleteAgentFromJSON(self,FormteurID):
        with open("Agents.json","r") as file:
            data = json.load(file)
        
        for record in data:
            if record["matricule"] == FormteurID:
                del data[data.index(record)]
        with open("Agents.json","w") as f:
            json.dump(data,f)
    
    def findAgentInJSON(self,FormateurID):
        with open("Agents.json","r") as file:
            data = json.load(file)
        
        for record in data:
            if record["matricule"] == FormateurID:
                return record
    
    def showAllAgent(self):
        with open("Agents.json","r") as file:
            data = json.load(file)
        return data
