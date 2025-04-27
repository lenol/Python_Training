import random
mon_random=random.randint(1, 100)
nombre_utilisateur=int(input("Saisir un nombre entier entre 1 et 100 :"))
print(nombre_utilisateur)
print(mon_random)
nombre_iteration=1
while nombre_utilisateur != mon_random :
	if mon_random<nombre_utilisateur :
		print("C'est moins")
		nombre_utilisateur=int(input("Saisir un nouveau nombre entier entre 1 et 100 :"))
	elif mon_random>nombre_utilisateur :
		print("C'est plus")
		nombre_utilisateur=int(input("Saisir un nouveau nombre entier entre 1 et 100 :"))
	nombre_iteration+=1
print(f"Bravo ! Tu as trouvé en {nombre_iteration} tentatives")