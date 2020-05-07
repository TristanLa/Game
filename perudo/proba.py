#On définit d comme la variable du nombre de dés du Perudo au total
#(au départ et restant en cours de jeu)
#On le définit via la nombre de joueur j, qui auront 5 dés chacun au départ
d = int(input("Combien de dés restant pour cette partie ? "))
print("Le nombre de dés est pour l'instant de ",d)

def fact(n):
    x = 1
    if n == 0:
        x = 1
    else:
        for i in range(n):
            x *= (i+1)
    return x

def combi(k, n):
    x = fact(n)/(fact(k)*fact(n-k))
    return int(x)

def binom(k, n, p):
    x = combi(k, n)*(p**(k))*((1-p)**(n-k))
    return x

def som_proba(k, n, p):
    x = 0
    for i in range(k,n+1):
        x = x + binom(i, n, p)
    return x

#On définit bet comme l''annonce en cours en termes de nombre de dés semblables (Entre 1 et d)
#et val comme la valeur des dés similaires annoncés (Entre 1 et 6)
#On définit p comme la probabilité qu''un dé obtiennent la face val
bet = int(input('Entrez le nombre de dés similaires annoncés par le joueur :'))
val = int(input("Entrez la valeur des dés de l'annonce :"))
if val == 1:
    p = (1/6)
else:
    p = (1/3)
print('La probabilité que le joueur ait EXACTEMENT raison est de', binom(bet, d, p)*100,'%')
print('La probabilité que le joueur ait raison est de', som_proba(bet, d, p)*100,'%')

#On prend en compte la main du joueur qui a l'ordi
#On note m le nombre de dés du joueur qui a l'ordi (Entre 1 et 5)
#On nomme t1, t2, ...., tm la valeur de chaque dé (compris entre 1 et 6)
m = int(input('Combien vous reste-t-il de dés ? '))
t = []
bet_real = bet
for i in range(m):
    t.append(int(input("Quelle est la valeur du dé {} ? ".format(i+1))))
    #On prend en retire les dés communs du joueur avec l'annonce faite (bet et val)
    if val == 1:
        if t[i] == 1:
            bet_real = bet_real-1
    else:
        if t[i] == 1 or t[i] == val:
            bet_real = bet_real-1
print("La probabilité que l'annonce soit EXACTEMENT bonne compte tenu de votre jeu est de", binom(bet_real, (d-m), p)*100,'%')
print("la probabilité que le joueur ait raison compte tenu de votre jeu est de", som_proba(bet_real, (d-m), p)*100,'%')