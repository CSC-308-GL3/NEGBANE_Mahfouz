from datetime import datetime
from Grade import Grade
from Employe import Employe
from Intervention import Intervention
from Client import Client
from Contrat import Contrat


# Création d'objets Grade
grade1 = Grade("A", "Technicien débutant", 15.0)
grade2 = Grade("B", "Technicien confirmé", 20.0)
grade3 = Grade("C", "Technicien expert", 25.0)

# Création d'objets Employé
employe1 = Employe(1001, "kokou", grade1, "01/01/2010")
employe2 = Employe(1002, "joacjin", grade2, "01/01/2005")
employe3 = Employe(1003, "francois", grade3, "01/01/2000")

# Création d'un objet Client
client1 = Client(1, "Client 1", "Adresse 1", "75000", "Paris", 50)

# Création d'un objet Contrat
contrat1 = Contrat(1, "01/01/2023", client1, 500.0)

# Création d'objets Intervention
intervention1 = Intervention(1, "10/01/2023", 3, 0.5, employe1)
intervention2 = Intervention(2, "20/01/2023", 2, 0.5, employe2)
intervention3 = Intervention(3, "30/01/2023", 4, 0.5, employe3)

# Ajout des interventions au contrat
contrat1.ajouterIntervention(intervention1)
contrat1.ajouterIntervention(intervention2)
contrat1.ajouterIntervention(intervention3)

# Calcul de l'écart entre le montant du contrat et le coût des interventions
ecart = contrat1.ecart()

print("Montant du contrat : ", contrat1.montantContrat)
print("Coût total des interventions : ")
print("Écart : ", ecart)
