"""
@package verses
@version 1.0
@author CN
@author Gudule
@date fev 2017


"""

try:
    import verse_parser
except Exception as e:
    import verses.verse_parser

# def analyze(text):
#     t = verse_parser.verse_parse(text, nbsyll=12, makecesure=True)
#     return t[0].analysis, t[0].counts

def is_alexandrin(lexitems, verbose=False):
    """
    La seule fonction à utiliser dans ce package.
    Vérifie directement si un vers donné est un alexandrin ou non,
    en utilisant la puissance du versificateur.

    Les hiatus sont acceptés. Toutes les autres erreurs (compte, diérèse)
    provoquent le rejet de l'alexandrin.
    """
    t = verse_parser.parse_tagged(lexitems, nbsyll=12, makecesure=True, verbose=verbose)
    return t
    # if len(t) != 1:
    #     return False
    # else:
    #     err = t[0].err
    #     if not err:
    #         return True
    #     else:
    #         for e in err:
    #             if e["message"] != verse_parser.HIATUS:
    #                 return False
    #         return True

