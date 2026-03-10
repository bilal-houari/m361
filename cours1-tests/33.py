class Vehicule:
    def __init__(self, marque):
        self.marque = marque

    def rouler(self):
        print(f"La {self.marque} avance.")


class Voiture(Vehicule):
    def __init__(self, marque, nb_portes):
        super().__init__(marque)
        self.nb_portes = nb_portes

    def klaxonner(self):
        print(f"la {self.marque} a klaxonne")


ma_voiture = Voiture("dacia", 5)

ma_voiture.rouler()
ma_voiture.klaxonner()
print(f"Nombre de portes : {ma_voiture.nb_portes}")
