
# coding: utf-8

# # Cryptanalyse

# ## Modalités d'attaque
# 
# Pour mesurer la résistance d'un chiffre à la cryptanalyse, on distingue les
# degrés d'intrusion suivants dans le sytème cryptographique :
# - chiffré seul : on connaît un chiffré.
# - clair connu : on connaît un ou plusieurs couples clair-chiffré.
# - clair choisi : on a accès à la fonction de chiffrement, que l'on peut étudier.
# - chiffré choisi : on a accès à la fonction de déchiffrement.
# 
# Un chiffre peut succomber à certaines attaques et résister à d'autres.
# Ces attaques étant toutes très plausibles, un chiffre doit être résistant
# pour chacune d'elles.

# ## Stratégies
# 
# Quelques stratégies classiques :
# - analyse fréquentielle + heuristiques
# - social engeneering (mot probable)
# - force brute
# 
# ## Attaque clair connu du chiffre de Hill
# 
# On sait que le chiffré suivant est de longueur 2 et commence par "LECO".

# In[77]:

c='DDKAHCUEWTSBRLWNUFKANQWK'


# In[78]:

[ ord(x)-ord('A') for x in 'LECO'],  [ ord(x)-ord('A') for x in 'DDKA']


# ## Cryptanalyse fréquentielle
# 
# L'observation à la base de toute la cryptologie classique est qu'une langue
# donnée utilise son alphabet de manière très biaisée : par exemple en francais
# la lettre E est de loin la plus fréquente (17%), suivie en général des lettres
# A, S, I, N, T, ...
# 
# Cela permet en général de résoudre un chiffre de César.

# In[55]:

def freq(s):
    c = {}
    for x in s:
        c[x] = c.get(x,0) + 1
    return sorted(c.items(),key=lambda x:x[1],reverse=True)


# In[56]:

c = 'VYXQDOWZCTOWOCESCMYEMRONOLYXXOROEBO'
freq(c)[:5]


# In[16]:

chr(65 + ord('O')-ord('E'))


# Avec un peu plus de travail, on résout de même le chiffre de Vigenère avec une simple analyse des lettres fréquentes.

# ## Force brute
# 
# Pour de petites tailles de blocs, une attaque par force brute paraît possible,
# mais quand il y a des milliers de possibilités il faut savoir reconnaître la clef valide.
# 
# Pour tout $a\in A$ on note $f_a(T)=\frac{n_a(T)}{n(T)}$ la fréquence d'apparition de $a$
# dans le texte $T$.
# 
# On introduit deux mesures pour discriminer les clefs de chiffres
# monoalphabétiques
# 
# - la somme des carrés $S(C,T) = \sum_a ( f_a(C)-f_a(T) )^2$
# - le test du chi2 (juste une renormalisation) $\chi^2(C,T) = \sum_a \bigl( 1-\frac{f_a(C)}{f_a(T)} \bigr)^2$
# 
# Dans une recherche par force brute, ces mesures permettent de classer les
# solutions par ordre de vraissemblance.

# In[ ]:




# Les fréquences sur les lettres ne suffisent toutefois pas à décrypter les
# chiffres de substitution, du fait que dans une langue donnée un certain nombre
# de lettres ont des fréquences très voisines.
# 
# On affine les choses en considérant aussi les fréquences de successions de deux
# lettres et trois lettres les plus fréquentes.
# 
# Par exemple, en français :
# - digrammes : ES, DE, LE, EN, RE, NT, ON, ER, TE, EL, AN
# - trigrammes : ENT, LES, EDE, DES, QUE, AIT, LLE, SDE
# 

# In[60]:

def ngrams(s,n=2,lmax=10):
    return freq([ s[i:i+n] for i in range(len(s)-n+1) ])


# In[61]:

s = """Le Lièvre considérant la Tortue qui marchait d'un pas tardif, et qui ne se traînait qu'avec peine,
se mit à se moquer d'elle et de sa lenteur. La Tortue n'entendit point raillerie, et lui dit d'un ton aigre,
qu'elle le défiait, et qu'elle le vaincrait à la course, quoiqu'il se vantât fièrement de sa légèreté.
Le Lièvre accepta le défi. Ils convinrent ensemble du lieu où ils devaient courir, et du terme de leur course.
Le Renard fut choisi par les deux parties pour juger ce différend. La Tortue se mit en chemin, et le Lièvre
à dormir, croyant avoir toujours du temps de reste pour atteindre la Tortue, et pour arriver au but avant elle.
Mais enfin elle se rendit au but avant que le Lièvre fut éveillé. Sa nonchalance l'exposa aux railleries des
autres Animaux. Le Renard, en Juge équitable, donna le prix de la course à la Tortue."""


# In[63]:

ngrams(s)[:5]


# On peut aussi se restreindre aux lettres a-z (à faire proprement en enlevant les accents d'abord, utiliser le module `unidecode`).

# In[65]:

s_ascii = ''.join(x for x in s.lower() if 'a'<=x<='z')
ngrams(s_ascii)[:5]


# In[ ]:




# In[ ]:



