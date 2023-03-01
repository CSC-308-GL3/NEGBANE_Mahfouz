class Client:
    def __init__(self, numero: int, nom: str, adresse: str, codePostal: str, ville: str, nbKm: int):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.codePostal = codePostal
        self.ville = ville
        self.nbKm = nbKm

    def distance(self) -> float:
        return self.nbKm