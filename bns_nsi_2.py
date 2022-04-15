def RechercheMinMax(l):
    if len(l) == 0:
        return {'min' : None, 'max' : None}
    d = {'min' : l[0], 'max' : l[0]}
    for e in l:
        if e < d['min']:
            d['min'] = e
        if e > d['max']:
            d['max'] = e
    return d

class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v
    """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str(self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"
    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]
        
class PaquetDeCarte:
    def __init__(self):
        self.contenu = []
    """Remplit le paquet de cartes"""
    def remplir(self):
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(1, 14)]
    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        if 0 <= pos < len(self.contenu) :
            return self.contenu[pos]
        
def maxi(l):
    if len(l) == 0:
        return None
    m = l[0]
    i = 0
    for e in range(1,len(l)):
        if l[e] > m:
            m = l[e]
            i = e
    return (m,i)

def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j+=1
        if j == g:
            trouve = True
        i+=1
    return trouve

def conv_bin(n):
    b = []
    i = 0
    while 2**i < n:
        i+=1
    for a in range(i,-1,-1):
        if 2**a <= n:
            n -= 2**a
            b.append(1)
        else:
            b.append(0)
    if b[0] == 0:
        del b[0]
    return b, len(b)

def tri_bulles(T):
    n = len(T)
    for i in range(n, -1,-1):
        for j in range(i):
            if T[j] > T[i]:
                temp = T[j]
                T[j] = T[i]
                T[j+1] = temp
    return T

