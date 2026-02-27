num1 = float(input("Entrez 1er nombre : "))
num2 = float(input("Entrez 2eme nombre : "))

print("1) addition")
print("2) soustraction")
print("3) multiplication")
print("4) division")

choice = input("Entrez operation (nombre) : ")

if choice == "1":
    print("Resultat :", num1 + num2)
elif choice == "2":
    print("Resultat :", num1 - num2)
elif choice == "3":
    print("Resultat :", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("Resultat :", num1 / num2)
    else:
        print("Erreur : division par zero")