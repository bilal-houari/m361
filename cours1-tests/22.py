class Voiture:
    def __init__(self, marque, modele, annee, kilometre=0, couleur="inconnue"):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometre = kilometre
        self.couleur = couleur

    def afficher_infos(self):
        return f"{self.marque} {self.modele} ({self.annee}) - {self.couleur} - {self.kilometre} km"


ma_voiture = Voiture("toyota", "Camry", 2002)
print(ma_voiture.afficher_infos())

voiture_pro = Voiture("renault", "golf", 2025, 888888, "gray")
print(voiture_pro.afficher_infos())
