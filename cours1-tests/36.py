class Personne:
    def __init__(self, nom):
        self.nom = nom

class Salarie(Personne):
    def __init__(self, nom, salaire):
        Personne.__init__(self, nom)
        self.salaire = salaire

class Etudiant(Personne):
    def __init__(self, nom, notes):
        Personne.__init__(self, nom)
        self.notes = notes

class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, salaire, notes):
        Salarie.__init__(self, nom, salaire)
        Etudiant.__init__(self, nom, notes)

doc = Doctorant("bilal", 817.50, [9.75, 10.08, 2.5])

print(f"nom: {doc.nom}")
print(f"salaire: {doc.salaire} dhs")
print(f"notes: {doc.notes}")