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

# nb1 = int(input("Entrez un premier nombre "))
# op = input("Entrez un operateur ")
# nb2 = int(input("Entrez un deuxieme nombre "))

# if op =="+":
#     print(nb1+nb2)
# elif op=="-":
#     print(nb1-nb2)
# elif op=='/':
#     if nb2 ==0:
#         print("on ne peut pas diviser par 0")
#     else:
#         print(nb1/nb2)
# elif op=="*":
#     print(nb1*nb2)

#endregion

#region note 

# noteUser = int(input("Veuillez entrer votre note"))

# if noteUser>=18 and noteUser<=20:
#     print("Felicitation")   
# elif noteUser>=10 and noteUser<18:
#     print("t'as reussis")  
# elif noteUser<10 and noteUser>=0:
#     print("je ne te félicite pas")
# else:
#     print('la note est en dehors des clous')   

# match noteUser:
#     case n if n>=18 and n<=20:
#         print("Felicitation")
#     case n if n>=10 and n<18:
#         print("t'as reussis")    
#     case n if n<10 and n>=0:
#         print("je ne te félicite pas")
#     case _:
#         print('la note est en dehors des clous')    



#endregion

#region convertisseur de seconde ameliorer

# dayUser=int(input('veuillez entrer le nombre de jour'))
# hourUser=int(input("veuillez entrer le nombre de d'heure"))
# minUser=int(input('veuillez entrer le nombre de minutes'))
# secUser=int(input('veuillez entrer le nombre de seconde'))
# totalMS = dayUser*86400 + hourUser*3600 + minUser*60+secUser

# dayUser=int(input('veuillez entrer le nombre de jour'))
# hourUser=int(input("veuillez entrer le nombre de d'heure"))
# minUser=int(input('veuillez entrer le nombre de minutes'))
# secUser=int(input('veuillez entrer le nombre de seconde'))
# totalMS2 = dayUser*86400 + hourUser*3600 + minUser*60+secUser

# totalMS = totalMS-totalMS2 if totalMS>totalMS2 else totalMS2-totalMS
# dayUser = totalMS//86400
# totalMS2 = totalMS%86400
# hourUser = totalMS2//3600
# totalMS2 = totalMS%3600
# minUser = totalMS2//60
# secUser = totalMS2%60

# print(f"la difference est de {dayUser} jours, {hourUser} heures, {minUser} minutes, {secUser} secondes")


#endregion

#region table de 2 

# i = 1
# while i <=10:
#     print(f"{i} x 2 = {i*2}")
#     i+=1


#endregion

#region modif lanceur de balle

# basket = int(input("Combien de balle dans le panier ? "))

# while basket>0:
#     ready = bool(int(input("Etes vous prêt ? 1 → oui , 0 → non")))
#     if ready:
#         print("Balle lancée")
#         basket -=1
#     else:
#         print("Vous n'etes pas prêt")
#         stop = bool(int(input('Voulez vous arreter maintenant ? 1 = oui 0 = non')))
#         if stop:
#             basket=0

# print("Panier vide")


#endregion

#region multipception

# i = 1
# while i <= 10:
#     j = 1 
#     while j <= 10:
#         print(f"{i} x {j} = {i*j}")
#         j +=1
#     i+=1


#endregion

#region au plus pret

# import random
# nbRandom = random.randrange(10)
# nbUser = int(input("Entrez un nombre"))
# while nbUser != nbRandom:
#     if nbUser< nbRandom:
#         print("c'est plus")
#         nbUser = int(input("Entrez un nombre"))
#     else:
#         print("c'est moin")
#         nbUser = int(input("Entrez un nombre"))
# print(f"Bravo le nombre etais {nbRandom}")

#endregion

#region tableau
# tab = []
# i = 0 
# j = 0
# while i<6:
#     tab.append(int(input(f"Veuiller entre le nombre n° {i+1}")))
#     i+= 1

# while j<len(tab):
#     print(tab[j])
#     j+=1
#endregion

#region tableau²
# i = 1
# j= 0
# tab = []
# while j<30:
#     i =i*2
#     tab.append(i)
#     j +=1
# j = 0
# while j<30:
#     print(tab[j])
#     j +=1
#endregion

#region cote joueur
"""
joueurs = int(input("Combien de joueurs ?(Max 10)"))
moyenne = 0
for j in range(0,joueurs,1):
    cote = int(input(f"Score n° {j}: "))
    moyenne +=cote
print(f"la moyenne des cotes de vos joueurs est : {moyenne/j}")
"""
#endregion

#region inversion tableau

# tab = [10,42,83]
# newTab = []

# for i in range(len(tab), 0,-1):
#     newTab.append(tab[i-1])
# for i in range(0, len(newTab), 1):
#     print(newTab[i])

#endregion

#region tri tableau

# tab = [42,18,27,74,56,1,96,24]

# for i in range(len(tab)) :
#     minimum= i
#     for j in range(i+1,len(tab)):
#         if tab[j]<tab[minimum]:
#             minimum = j
#     tab[i],tab[minimum] = tab[minimum], tab[i]
# for i in range(0,len(tab),1):
#     print(tab[i])

#endregion
