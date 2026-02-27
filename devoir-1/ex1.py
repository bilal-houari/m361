age = int(input("Entrez age : "))

if age <= 12:
    print("Vous etes un enfant")
elif age <= 17:
    print("Vous etes un adolescent")
elif age <= 64:
    print("Vous etes un adulte")
else:
    print("Vous etes un senior")