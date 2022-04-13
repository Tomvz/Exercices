def recherche(c, m):
    somme = 0
    for l in m:
        if l == c:
            somme+=1
    return somme

Pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)

def moyenne(l):
    somme = 0
    coeff = 0
    for t in l:
        somme+= t[1] * t[0]
        coeff+=t[1]
    return somme / coeff


def pascal(n):
    C= [[1]]
    for k in range(1,n):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C

def delta(t):
    nt = [t[0]]
    for v in range(1, len(t)):
        nt.append(t[v]-t[v-1])
    return nt

class Noeud:
    '''
    Classe implémentant un noeud d'arbre binaire disposant de 3 attributs :
    - gauche : le sous-arbre gauche.
    - valeur : la valeur de l'étiquette,
    - droit : le sous-arbre droit.
    '''
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
        
    def __str__(self):
        return str(self.valeur)
    
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None
    
    def expression_infixe(e):
        s = ''
        if e.gauche is not None:
            s = '(' + s + Noeud.expression_infixe(e.gauche)
        s = s + str(e.valeur)
        if e.droit is not None:
            s = s + Noeud.expression_infixe(e.droit) + ')'
        if e.est_une_feuille():
            return s
        return s
        
def recherche2(l):
    c = []
    for i in range(1, len(l)):
        if l[i] == l[i-1] + 1:
            c.append((l[i-1], l[i]))
    return c

def propager(M, i, j, val):
    if M[i][j]== 0:
        return
    M[i][j]=val
# l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)
# l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)
# l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)
# l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j+1, val)
        


tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]

resultat = {'min': None, 'max': None}

def rechercheMinMax(tableau):
    mini = tableau[0]
    for i in range(0,len(tableau)):
       if tableau[i] < mini:
           mini = tableau[i]
           
       tableau.remove()
       