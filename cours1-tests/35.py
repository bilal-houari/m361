class Vehicule:
    def demarrer(self):
        print("demarrage vehicule")

class Voiture(Vehicule):
    def demarrer(self):
        print("voiture demarre")

class Moto(Vehicule):
    def demarrer(self): 
        print("moto demarre")

ma_voiture = Voiture()
ma_moto = Moto()

ma_voiture.demarrer()
ma_moto.demarrer()  