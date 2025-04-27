phrase_utilisateur=input()
mes_occurences_de_chaque_voyelles = {"a":0, "e":0, "i":0, "o":0, "u":0, "y":0}
compteur=0
for i in range(len(phrase_utilisateur)):
    if phrase_utilisateur[i]=="a":
        compteur+=1
        mes_occurences_de_chaque_voyelles["a"]+=1
    elif phrase_utilisateur[i]=="e":
        compteur+=1
        mes_occurences_de_chaque_voyelles["e"]+=1
    elif phrase_utilisateur[i]=="i":
        compteur+=1
        mes_occurences_de_chaque_voyelles["i"]+=1
    elif phrase_utilisateur[i]=="o":
        compteur+=1
        mes_occurences_de_chaque_voyelles["o"]+=1
    elif phrase_utilisateur[i]=="u":
        compteur+=1
        mes_occurences_de_chaque_voyelles["u"]+=1
    elif phrase_utilisateur[i]=="y":
        compteur+=1
        mes_occurences_de_chaque_voyelles["y"]+=1
print(compteur)
print("a: "+str(mes_occurences_de_chaque_voyelles["a"])+" fois,"+"e: "+str(mes_occurences_de_chaque_voyelles["e"])+" fois," + "i: "+str(mes_occurences_de_chaque_voyelles["i"])+" fois,"+"o: "+str(mes_occurences_de_chaque_voyelles["o"])+" fois,"+"u: "+str(mes_occurences_de_chaque_voyelles["u"])+" fois,"+"y: "+str(mes_occurences_de_chaque_voyelles["y"])+" fois")