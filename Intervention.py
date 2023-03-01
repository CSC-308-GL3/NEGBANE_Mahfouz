from Employe import Employe
class Intervention:
  def __init__(self, numero: int, date: str, duree: int, tarifKm: float, technicien: Employe):
    self.numero = numero
    self.date = date
    self.duree = duree
    self.tarifKm = tarifKm
    self.technicien = technicien

  def affiche(self):
    print("Intervention numéro :", self.numero)
    print("Date :", self.date)
    print("Durée :", self.duree)
    print("Tarif kilométrique retenu :", self.tarifKm)
    print("Technicien :", self.technicien.nom, "-", self.technicien.prenom)

  def fraisKm(self, dist: float) -> float:
    return dist * self.tarifKm

  def fraisMo(self) -> float:
    return self.technicien.coutHoraire() * self.duree

