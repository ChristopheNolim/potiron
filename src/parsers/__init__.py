"""
@package parsers
@version 1.0
@author CN
@author Gudule
@date fev 2017

Ce package est directement importé du versificateur, un autre projet de
CN et Gudule. Il s'agit d'une version plus avancée pour le moment.

@todo pour l'instant, ne traite que les alexandrins. Faire plus ne demanderait
pas beaucoup d'effort.

Provides parsers for the French language.

@see text_parser.py
@see verse_parser.py
"""

try:
    import verse_parser
except Exception as e:
    import parsers.verse_parser

def analyze(text):
    t = verse_parser.verse_parse(text, nbsyll=12, makecesure=True)
    return t[0].analysis, t[0].counts

def is_alexandrin(text):
    """
    La seule fonction à utiliser dans ce package.
    Vérifie directement si un vers donné est un alexandrin ou non,
    en utilisant la puissance du versificateur.

    (Cet usage est très sub-optimal, mais bien cloisonné).

    Les hiatus sont acceptés. Toutes les autres erreurs (compte, diérèse)
    provoquent le rejet de l'alexandrin.
    """
    t = verse_parser.verse_parse(text, nbsyll=12, makecesure=True)
    if len(t) != 1:
        return False
    else:
        err = t[0].err
        if not err:
            return True
        else:
            for e in err:
                if e["message"] != verse_parser.HIATUS:
                    return False
            return True

