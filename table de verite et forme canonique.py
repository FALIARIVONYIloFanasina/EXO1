#PROGRAMME TABLE DE VERITE

#Exemple pour n = 2
#Pour la fonction logique: F = A*B + notA*notB

n = int(input("Entrer le nombre de variables : "))
m = 2**n
print("Les combinaisons possibles sont:", m)

fonction = "F = A*B + notA*notB"
print("Donner une fonction logique: ", fonction)

print("La table de verite est: ")

#Afficher l'en-tête du tableau
print("A |B  |notA  |notB   |A*B   |notA*notB    | F ")
print("-" * 44)

def lignes_du_tableau(A, B):
    if A == 1:
        notA = 0
    else:
        notA = 1
    if B == 1:
        notB = 0
    else:
        notB = 1
    F = A * B + notA * notB

    print(A ,"|",B  ,"|",notA  ,"  ","|",notB  ,"    ","|",A*B  ," ","|",notA*notB  ,"         ","|", F)

lignes_du_tableau(1, 1)
lignes_du_tableau(1, 0)
lignes_du_tableau(0, 1)
lignes_du_tableau(0, 0)

#PROGRAMME FORME CANONIQUE
#Pour la fonction F précédente

print("La première forme canonique est: F = A*B + notA*notB")
print("La seconde forme canonique est: F = (notA + B)(A + notB)")