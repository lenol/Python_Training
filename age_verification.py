import sys
entree_utilisateur=input("Quel est votre age ? ")
if entree_utilisateur=="stop":
    sys.exit("Au revoir !")
else :
    while entree_utilisateur!="stop":
        try:
            age=int(entree_utilisateur)
            if age<18 :
                print("Mineur")
            elif age<=65 :
                print("Adulte")
            else :
                print("Senior")
        except ValueError:
            print("Veuillez entrer un âge valide ou 'stop' pour quitter.")
        entree_utilisateur=input("Quel est votre age ? ")