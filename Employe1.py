from abc import ABC, abstractmethod
from datetime import datetime
from IEmploye import IEmploye
from  exame2   import IR

class Employe(IEmploye,IR,ABC):
    count = 0
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase):
        count += 1
        self.mtle = mtle
        self.nom = nom

        d = datetime.strptime(dateNaissance)
        self.dateNaissance = d
        
        d = datetime.strptime(dateEmbuche)
        self.dateEmbuche = d
        self.salaireBase = salaireBase
    
    @property
    def mtle(self):
        return self.mtle 
    
    @property
    def nom(self):
        return self.nom 
    @nom.setter
    def nom(self,nom):
        self.nom= nom

    @property
    def dateNaissance(self):
        return self.dateNaissance 
    @dateNaissance.setter
    def dateNaissance(self,dateNaissance):
        self.dateNaissance= dateNaissance

    @property
    def dateEmbuche(self):
        return self.dateEmbuche 
    @dateEmbuche.setter
    def dateEmbuche(self,dateEmbuche):
        self.dateEmbuche= dateEmbuche

    @property
    def salaireBase(self):
        return self.salaireBase 
    @salaireBase.setter
    def salaireBase(self,salaireBase):
        self.salaireBase= salaireBase

    def age(self):
        todayDate = datetime.date.today()
        age = todayDate.year - self.dateNaissance.year
        return age
    
    def dateRetrait(self, ageRetrait):
        return self.dateNaissance - datetime.strptime(ageRetrait+"/01/"+"01")
        
    def anciennete(self):
        todayDate = datetime.date.today()
        anc = todayDate.year - self.dateEmbuche.year
        return anc
    def isAncienneteGreaterthan20year(self):
        if self.anciennete() > 20:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.mtle} - {self.nom} - {self.dateNaissance} - {self.dateEmbuche} - {self.salaireBase} "

    def __eq__(self,e):
        if self.mtle == e.mtle:
            return True
        else :
            return False
        
    @abstractmethod
    def salaireAPayer():
        pass     