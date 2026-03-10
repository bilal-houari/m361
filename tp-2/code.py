from abc import ABC, abstractmethod
from dataclasses import dataclass


class Boisson(ABC):
    @abstractmethod
    def cout(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    def __add__(self, other):
        if isinstance(other, Boisson):
            return BoissonCombinee(self, other)
        return NotImplemented


class Cafe(Boisson):
    def cout(self):
        return 20.0

    def description(self):
        return "cafe simple"


class The(Boisson):
    def cout(self):
        return 11.5

    def description(self):
        return "the"


class BoissonCombinee(Boisson):
    def __init__(self, b1: Boisson, b2: Boisson):
        self.b1 = b1
        self.b2 = b2

    def cout(self):
        return self.b1.cout() + self.b2.cout()

    def description(self):
        return f"{self.b1.description()} et {self.b2.description()}"


class DecorateurBoisson(Boisson):
    def __init__(self, boisson: Boisson):
        self.boisson = boisson


class Lait(DecorateurBoisson):
    def cout(self):
        return self.boisson.cout() + 1.5

    def description(self):
        return self.boisson.description() + ", lait"


class Sucre(DecorateurBoisson):
    def cout(self):
        return self.boisson.cout() + 0.5

    def description(self):
        return self.boisson.description() + ", sucre"


class Caramel(DecorateurBoisson):
    def cout(self):
        return self.boisson.cout() + 2.5

    def description(self):
        return self.boisson.description() + ", caramel"


@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int


class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson: Boisson):
        self.boissons.append(boisson)

    def calculer_total(self):
        return sum(b.cout() for b in self.boissons)

    def afficher_commande(self):
        print(
            f"Commande pour {self.client.nom} : ////////////////////////////////////////"
        )
        for b in self.boissons:
            print(f"- {b.description()} : {b.cout()} DH")
        print(f"total : {self.calculer_total()} DH")


class CommandeSurPlace(Commande):
    def afficher_commande(self):
        print("(sure place) :")
        super().afficher_commande()


class CommandeEmporter(Commande):
    def afficher_commande(self):
        print("(a emporter) :")
        total = self.calculer_total() + 10  # frais
        super().afficher_commande()
        print(f"total : {total} DH")


class Fidelite:
    def ajouter_points(self, client: Client, montant):
        nouveaux_points = int(montant)
        client.points_fidelite += nouveaux_points
        print(
            f"points fidelite ajoutes : {nouveaux_points}. total : {client.points_fidelite}"
        )


class CommandeFidele(Commande, Fidelite):
    def valider_commande(self):
        total = self.calculer_total()
        self.ajouter_points(self.client, total)
        print("commande avec fidelite")


client1 = Client("bilal", 12121, 500)

cafe1 = Sucre(Lait(Cafe()))
the1 = Caramel(The())

mix = Cafe() + The()

commande1 = CommandeFidele(client1)
commande1.ajouter_boisson(cafe1)
commande1.ajouter_boisson(the1)
commande1.ajouter_boisson(mix)

commande1.afficher_commande()

commande1.valider_commande()
