class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("entez age entier")
        if valeur < 0:
            raise ValueError("age negative")
        if valeur > 150:
            raise ValueError("age irrealiste")
        self._age = valeur


p1 = Personne("bilal", 65)
print(f"{p1._nom} a {p1.age} ans.")

p1.age = 66
print(f"modification : {p1.age} ans.")

try:
    p1.age = -5
except ValueError as e:
    print(f"error : {e}")

try:
    p1.age = "haha"
except TypeError as e:
    print(f"eror : {e}")

try:
    Personne("bilal", 1662)
except ValueError as e:
    print(f"error : {e}")
