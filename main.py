"""Module contenant l'implémentation itérative et récursive de l'algorithme
d'encodage Run-Length (artcode)."""

import sys
sys.setrecursionlimit(2000)


def artcode_i(s):
    """Encode une chaîne en une liste de tuples (caractère, nombre d'occurrences)
    en utilisant une approche itérative.

    Args:
        s (str): chaîne à encoder

    Returns:
        list[tuple[str, int]]: liste des couples (caractère, répétitions)
    """
    retour = s[0]
    k = 1
    result = []

    for i in range(1, len(s)):
        if s[i] == retour:
            k += 1
        else:
            result.append((retour, k))
            k = 1
        retour = s[i]

    result.append((retour, k))
    return result


def artcode_r(s):
    """Encode une chaîne en une liste de tuples (caractère, nombre d'occurrences)
    en utilisant une approche récursive.

    Args:
        s (str): chaîne à encoder

    Returns:
        list[tuple[str, int]]: liste des couples (caractère, répétitions)
    """
    if not s:
        return []

    i = 1
    while i < len(s) and s[i] == s[0]:
        i += 1

    return [(s[0], i)] + artcode_r(s[i:])


def main():
    """Fonction principale exécutant quelques tests de l'encodeur."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))


if __name__ == "__main__":
    main()
