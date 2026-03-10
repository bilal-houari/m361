class Voiture:
    def __init__(self, marque, modele, code_moteur):
        self.marque = marque
        self.modele = modele
        self.__code_moteur = code_moteur

    def verifier_moteur(self):
        return f"diagnostic du moteur {self.__code_moteur} termine"


ma_voiture = Voiture("dacia", "sandero", "16165165")

try:
    print(ma_voiture.__code_moteur)
except AttributeError:
    print("eror")

print(ma_voiture.verifier_moteur())

print(f"code forcement lu : {ma_voiture._Voiture__code_moteur}")