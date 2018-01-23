
# coding: utf-8

# # Chiffres classiques

# ## Alphabet
# 
# On définit l'ensemble de symboles sur lequel opère un cryptosystème. Pour la suite, il est bien que ce soit un anneau,
# on prendra $\mathbb Z/n\mathbb Z$.

# In[126]:

class Code:
    mod = 26
    def encode(self,data): pass
    def decode(self,data): pass


# Par exemple on envoie les lettres de l'alphabet dans
# l'anneau $\mathbb Z/26\mathbb Z$.

# In[127]:

class Alphabet(Code):
    A = ord('A')

    def encode(self,s):
        return [ ord(c)-self.A for c in s.upper() if 'A' <= c <= 'Z' ]

    def decode(self,l,j=''):
        return j.join( [ chr(c+self.A) for c in l ])


# ## Cryptosystème
# 
# Pour définir un cryptosystème ci-dessous, on fournit une fonction de chiffrement et une fonction de déchiffrement.

# In[84]:

class Chiffre:
    clef = None
    code = Alphabet()

    def _chiffre(self, m): pass

    def _dechiffre(self, c): pass

    def chiffre(self, clair):
        # codage sur l'alphabet
        M = self.code.encode(clair)
        # chiffrement
        C = [ self._chiffre(m) for m in M ]
        # décodage
        return self.code.decode(C)

    def dechiffre(self, chiffre):
        C = self.code.encode(chiffre)
        M = [ self._dechiffre(c) for c in C ]
        return self.code.decode(M)


# ### Le chiffre de César

# In[85]:

class Cesar(Chiffre):
    def __init__(self, clef):
        self.code = Alphabet()
        self.clef = self.code.encode(clef)[0]

    def _chiffre(self, m):
        return (m + self.clef) % self.code.mod

    def _dechiffre(self, c):
        return (c - self.clef) % self.code.mod


# In[86]:

C = Cesar('k')
C.chiffre("longtempsjemesuiscouchedebonneheure")


# In[87]:

C.dechiffre('VYXQDOWZCTOWOCESCMYEMRONOLYXXOROEBO')


# ### Le chiffre affine

# In[88]:

class Affine(Chiffre):
    
    def __init__(self, a, b):
        self.code = Alphabet()
        self.clef = (a,b)

    def _chiffre(self, m):
        a,b = self.clef
        return (a * m + b) % self.code.mod


# In[89]:

A = Affine(3,12)
A.chiffre("longtempsjemesuiscouchedebonneheure")


# Exercice : écrire la méthode de déchiffrement (restreindre si besoin l'espace des clefs).

# ### Le chiffre par substitution

# In[90]:

class Substitution(Chiffre):
    
    def __init__(self):
        import random
        self.clef = list(range(self.code.mod))
        random.shuffle(self.clef)
        
    def _chiffre(self, m):
        return self.clef[m]


# In[91]:

S = Substitution()
S.chiffre("lebonlabruteetletruan")


# Exercice: écrire aussi le déchiffrement.

# ## Chiffres par blocs

# La plupart des cryptosystèmes opèrent sur des blocs
# de plusieurs lettres.

# In[92]:

class Block(Alphabet):
    def __init__(self, length, alphabet):
        self.l = length
        self.alphabet = alphabet

    # scinde une liste en blocs de l éléments
    def encode(self, s):
        s = self.alphabet.encode(s)
        return [ s[i:i+self.l] for i in range(0, len(s), self.l) ]

    # concatène
    def decode(self, l):
        return self.alphabet.decode(sum(l, []))


# ### Le chiffre de Vigenère

# C'est un chiffre de César par blocs.

# In[104]:

class Vigenere(Chiffre):

    def __init__(self, clef):
        AZ = Alphabet()
        self.clef = AZ.encode(clef)
        self.code = Block(len(self.clef), AZ)

    def _chiffre(self, clair):
        return [ (c+k) % self.code.mod for c,k in zip(clair,self.clef) ]


# In[125]:

V = Vigenere("clef")
c = V.chiffre("onvoiticiquelesjeunesgenssurtoutlesjeunesfillesbellesbienfaitesetgentilles")
' '.join([c[i:i+4] for i in range(0,len(c),4)])


# ### Le Chiffre de Hill
# 
# C'est une application affine $A^l\to A^l$,
# que l'on peut représenter matriciellement.

# In[101]:

class Hill(Chiffre):

    def __init__(self, length, clef):
        self.code = Block(length, Alphabet())
        self.clef = self.code.encode(clef)
        assert len(self.clef) == length

    def _chiffre(self, m):
        return [ sum( x * y for x,y in zip(k,m) ) % self.code.mod for k in self.clef ]


# In[102]:

H = Hill(3,'baaabaaab')
H.chiffre('lavillesendormaitjenoublielenom')


# In[118]:

H = Hill(3,'vxbufacri')
H.chiffre('lavillesendormaitjenoublielenom')


# ## Modes de chiffrement par blocs
#     

# In[98]:

class ChiffreCBC(Chiffre):
    
    def chiffre(self, clair):
        # codage sur l'alphabet
        M = self.code.encode(clair)
        # chiffrement
        C = [ self._chiffre(M[0]) ]
        for i in range(1,len(M)):
            C.append(self._chiffre(M[i]+C[i-1]))
        # décodage
        return self.code.decode(C)


# In[ ]:



