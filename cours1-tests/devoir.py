class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

personne1 = Personne('bilal', 56, 'bilal@email.com')
print(f"nom: {personne1.nom}")      
print(f"age: {personne1.age}")      
print(f"email: {personne1.email}")  

personne1.nom = 'bilal houari'                    
personne1.age += 10                                   
personne1.email = 'bilal.houari@email.com'     

print(f"nv nom: {personne1.nom}")  
print(f"nv age: {personne1.age}")    