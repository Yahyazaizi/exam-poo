from abc import ABC, abstractmethod
class IEmploye(ABC):
    @abstractmethod
    def age(self):
        pass 
    @abstractmethod
    def anciennete(self):
        pass
    @abstractmethod
    def dateRetrait(self,ageRetrait):
        pass