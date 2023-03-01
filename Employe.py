from Grade import Grade
from datetime import date
class Employe:
    def __init__(self, numero: int, nom: str, qualification: Grade, dateEmbauche: str):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.dateEmbauche = dateEmbauche

    def coutHoraire(self) -> float:
        anciennete = self.getAnciennete(self.dateEmbauche)
        if anciennete < 5:
            coefficient = 1.0
        elif anciennete < 11:
            coefficient = 1.05
        elif anciennete < 16:
            coefficient = 1.08
        else:
            coefficient = 1.12
        return self.qualification.tauxHoraire() * coefficient

    def getNumero(self) -> int:
        return self.numero

    def getNom(self) -> str:
        return self.nom

    def getQualification(self) -> Grade:
        return self.qualification

    def getDateEmbauche(self) -> str:
        return self.dateEmbauche

    def getAnciennete(self, dateEmbauche: str) -> int:
        annee_embauche = int(dateEmbauche.split('/')[2])
        mois_embauche = int(dateEmbauche.split('/')[1])
        jour_embauche = int(dateEmbauche.split('/')[0])
        date_embauche = date(annee_embauche, mois_embauche, jour_embauche)
        today = date.today()
        anciennete = today.year - date_embauche.year - ((today.month, today.day) < (date_embauche.month, date_embauche.day))
        return anciennete
