from Client import Client
from Intervention import Intervention
class Contrat:
    def __init__(self, numero: int, date: str, client: Client, montantContrat: float):
        self.numero = numero
        self.date = date
        self.client = client
        self.montantContrat = montantContrat
        self.interventions = []
        self.nbIntervention = 0
        
    def ecart(self) -> float:
        totalCost = sum([intervention.fraisMo() for intervention in self.interventions])
        return self.montantContrat - totalCost
    def montantContrat(self):
        return self.ecart() + sum([intervention.fraisMateriel() for intervention in self.interventions])
    
    def coutTotal(self):
        return sum([intervention.cout() for intervention in self.interventions])

    def ajouterIntervention(self, intervention: Intervention):
        self.interventions.append(intervention)
        self.nbIntervention += 1