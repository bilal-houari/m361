class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je suis {self.nom}, {self.age} ans"


p1 = Personne("Houari", 64)
p2 = Personne("Bilal H", 63)

print(p1.se_presenter())
print(p2.se_presenter())