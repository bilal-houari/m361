contacts = ["Bouchra", "Ahmed", "Sara"]

while True:
    print("1) ajouter un contact")
    print("2) afficher les contacts")
    print("3) quitter")
    
    choice = input("Choisir (1,2,3) : ")
    
    if choice == "1":
        name = input("nom du contact : ")
        contacts.append(name)
    elif choice == "2":
        for i, name in enumerate(contacts, 1):
            print(i, name)
    elif choice == "3":
        break
    else:
        print("invalide")