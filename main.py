#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    retour = s[0]
    k = 1
    result = []

    for i in range(1, len(s)) :
        if s[i] == retour :
            k = k + 1
        else : 
            result.append( (retour, k) )
            k = 1
        retour = s[i]
    result.append( (retour, k) )
    return result


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici

    # cas de base
    if not s :
        return []
    i = 1
    # recherche nombre de caractères identiques au premier
    while i < len(s) :
        
        if s[0] == s[i] :
            i = i + 1
        else :
            break


    # appel récursif

    return [(s[0], i) ] + artcode_r(s[i::])
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
