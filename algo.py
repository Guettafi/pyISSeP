#region exo1
# a=5
# b=7

# c=a
# a=b
# b=c

# print(f"le resultat de a :{a} et b:{b}")
# print("le resultat de a : " +a+" et b: "+b)

#endregion

#region exo2

# prenom = input('Entre votre prenom ')
# nom = input('Entrez votre nom ')
# age = input('Entrez votre age')
# print(f"Bonjour {prenom} {nom}, j'ai {age} ans")
# print("Bonjour "+prenom+ ', ' +nom+ " j'ai "+age+" ans")

#endregion

#region exo 3

# Convertisseur de seconde, 4561 = 0j, 1h, 16min, 1sec

# secUser = int(input('Entrez un nombre de secondes '))
# jour = secUser//86400
# reste = secUser%86400
# hour = reste//3600
# reste = reste%3600
# minutes = reste//60
# sec = reste%60

# print(f" Votre entrée donne : {jour}j, {hour}h, {minutes}min, {sec}sec.")

#endregion

#region annee Bissextile

# yearUser = int(input("Entrez une annee "))

# if (yearUser%4 == 0 and yearUser%100 != 0) or yearUser%400==0 : 
#     print("Elle est bissextile")
# else:
#     print("Elle n'est pas bissextile")

#endregion

#region lanceur de balle

# empty = bool(int(input("Le panier est-il vide ? 1 → oui , 0 → non")))

# if not empty :
#     ready = bool(int(input("Etes vous prêt ? 1 → oui , 0 → non")))
#     if ready:
#         print("preparer vous a jouer")
#     else:
#         print("Vous n'etes pas prêt")
# else:
#     print("panier vide")


#endregion

#region Distributeur

# choice = int(input("Pour du coca taper 1, pour du fanta taper 2, pour de l'ice-tea taper 3, pour de l'eau taper 4"))

# drink1 = 42
# drink2 = 18
# drink3 = 0
# drink4 = 0


# if choice ==1 and drink1>0:
#     print("voici votre coca")
#     drink1-=1
# elif choice == 2 and drink2>0:
#     print("voici votre fanta")
#     drink2-=1
# elif choice == 3 and drink3>0:
#     print("voici votre icetea")
#     drink3-=1
# elif choice == 4 and drink4>0:
#     print("voici votre eau")
#     drink4-=1
# else:
#     print("Votre choix n'est soit plus de stock soit pas disponnible dans notre distributeur")



# match choice :
#     case 1 if drink1>0:
#         print("Vous avez choisis le coca")
#         drink1-=1
#     case 2 if drink2>0:
#         print("Vous avez choisis le fanta")
#         drink2-=1
#     case 3 if drink3>0:
#         print("Vous avez choisis l'ice-tea")  
#         drink3-=1  
#     case 4 if drink4>0:
#         print("Vous avez choisis de l'eau")
#         drink4-=1
#     case _:
#         print("le choix que vous avez fait n'est pas disponnible dans notre distributeur ou nous n'avons plus de stock ")



#endregion

#region calculatrice


#endregion


