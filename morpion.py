# # 16/08

# grille = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0],
# ]

# def affichegrille(grille):
#     graph = []

#     for ligne in grille:
#         for item in ligne:
#             if item == 0 :
#                 graph.append(" ")
#             if item == 1 :
#                 graph.append("x")
#             if item == 2 :
#                 graph.append("o")
                
#     for i in range(len(graph)):
#         if i==2 or i==5 or i==8:
#             print(f" {graph[i-2]} | {graph[i-1]} | {graph[i]} ")
#             print('\n')
            

# def askligne(ligne):
#     precligne = input("laulau?: ")
#     return int(precligne) - 1
    
# def askcolonne(colonne):
#     preccolonne = input("colonne?: ")
#     return int(preccolonne) - 1
    
# def askjeu():
#     prec = input("x ou o: ")
#     if prec == "x" :
#         return 1
#     if prec == "o" :
#         return 2
    
# def victoire(grille):
#     if (grille[0][0]==grille[0][1]==grille[0][2] and grille[0][0]!=0) or (grille[1][0]==grille[1][1]==grille[1][2] and grille[1][0]!=0) or (grille[2][0]==grille[2][1]==grille[2][2] and grille[2][0]!=0) :
#         print("victoire par ligne")
#         affichegrille(grille)
#         return 1
    
#     if (grille[0][0]==grille[1][0]==grille[2][0] and grille[0][0]!=0) or (grille[0][1]==grille[1][1]==grille[2][1] and grille[0][1]!=0) or (grille[0][2]==grille[1][2]==grille[2][2] and grille[0][2]!=0) :
#         print("victoire par colonne")
#         affichegrille(grille)
#         return 1
        
#     if (grille[0][0]==grille[1][1]==grille[2][2] and grille[0][0]!=0) or (grille[0][2]==grille[1][1]==grille[2][2] and grille[0][2]!=0) :
#         print("victoire par diago")
#         affichegrille(grille)
#         return 1
    
#     return 0
    
    
# def jeu():
    
#     ligne = 0
#     colonne = 0
    
#     affichegrille(grille)

#     while not (victoire(grille)) :
#         ligne = askligne(ligne)
#         colonne = askcolonne(colonne)
#         grille[ligne][colonne] = askjeu()
#         affichegrille(grille)
        
#     return 0


# jeu()

import tkinter as tk
import tkinter.messagebox as messagebox


# Crée une fenêtre principale
root = tk.Tk()
root.title("Morpion")

# Variables pour suivre l'état de la grille
grille = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

joueur_actuel = "X"  # Le premier joueur est "X"

# Fonction pour vérifier la victoire
def verifie_victoire():
    for ligne in grille:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != 0:
            return True

    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] and grille[0][col] != 0:
            return True

    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != 0:
        return True

    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] != 0:
        return True

    return False

# Fonction pour afficher un message de victoire
def affiche_victoire(joueur):
    messagebox.showinfo("Victoire", f"Le joueur {joueur} a gagné !")
    root.quit()

# Fonction pour gérer les clics sur les boutons
def bouton_clic(ligne, colonne):
    global joueur_actuel

    # Si la case est vide, on la remplit avec le symbole du joueur actuel
    if grille[ligne][colonne] == 0:
        grille[ligne][colonne] = joueur_actuel
        boutons[ligne][colonne].config(text=joueur_actuel)

        # Vérification de la victoire
        if verifie_victoire():
            affiche_victoire(joueur_actuel)
            root.quit()  # Ferme la fenêtre après la victoire

        # Changer de joueur
        joueur_actuel = "O" if joueur_actuel == "X" else "X"

# Création de la grille de boutons
boutons = []

for i in range(3):
    ligne_boutons = []
    for j in range(3):
        bouton = tk.Button(root, text="", width=10, height=3, command=lambda i=i, j=j: bouton_clic(i, j))
        bouton.grid(row=i, column=j)  # Positionne les boutons dans une grille
        ligne_boutons.append(bouton)
    boutons.append(ligne_boutons)

# Lancer la fenêtre
root.mainloop()


