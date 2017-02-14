
"""
@file src/verses/verse_parser.py
@version 1.0
@author CN
@author Gudule
@date fev 2017

Ce code a été adapté du versificateur, un autre projet.
On tient compte ici du fait que les LexiconItem contiennent déjà les informations
utiles (nombre de syllabes, diérèses, h aspirés).

"""


#====================
# Message correspondant à un hiatus
#==================

HIATUS = "Hiatus"

#====================
# Message correspondant à une mauvaise césure
#==================

CESURE = "Cesure"

#=======================
# Mauvais compte de syllabes
#=========================

NBSYLL = "Nbsyll"

#================================

VOYELLES = "aeiouyâàäéèêëùûüîïôöœÿ"


def parse_tagged(lexitems, nbsyll=12, makecesure=True, verbose=False):
    """
    Parse un vers et vérifie qu'il est bien formé. Juste besoin de retourner un
    booléen (contrairement au versificateur).
    """

    words = [ t for t in lexitems if t["gram"] not in ["PUN", "SEN"] ]
    if not words:
        return False

    err = []
    current_word = words[0]

    if verbose:
        print(current_word)

    if current_word["hasdie"]:
        counts = [[current_word["count"]], [current_word["count"] + 1]]
    else:
        counts = [[current_word["count"]]]

    # normalement : si w est une ponctuation, count sera 0 de toute façon
    for w in words[1:]:
        if verbose:
            print(w)
        # print(w)
        # print(counts)
        # compter le nouveau mot
        counts = [ l + [l[-1] + w["count"]] for l in counts ]

        if w["hasdie"]:
            # ajouter une possibilité de diérèse
            counts = counts + [ c[:-1] + [c[-1] + 1] for c in counts]

        # règle du hiatus plutôt permissive
        # une règle plus stricte serait : not current_word["endsemuet"] (donc il faudrait forcément finir par un e muet)
        if w["orth"][0] in VOYELLES and current_word["orth"][-1] in VOYELLES and current_word["orth"][-1] != "e":
            # ici c'est quand même une élision
            # (oui, on a tué l'apostrophe...)
            if not current_word["orth"].endswith("qu"):
                err.append(HIATUS)
        if w["orth"][0] in VOYELLES and current_word["emuet"]:
        # if next_word["beginsvoy"] and current_word["endsemuet"]:
            # retirer une syllabe par élision du e muet
            # la retirer aussi sur le vers précédent (!!!) sinon problèmes de césure
            # counts[-1] = counts[-1][0] - 1, counts[-1][1] - 1
            counts = [ l[:-2] + [l[-2] - 1, l[-1] - 1]  for l in counts ]

        current_word = w

    # la dernière syllabe est muette
    if current_word["syllmuette"]:
        counts = [ l[:-1] + [l[-1] - 1]  for l in counts ]

    if verbose:
        print(counts)

    if nbsyll is not None:
        check = _check_counts(words, counts, nbsyll, makecesure)
        if check is not None:
            err.append(check)

    for e in err:
        if e != HIATUS:
            # ce n'est pas un bon vers
            return False
    # c'est un bon vers
    return True


def _check_counts(lexitems, counts, nbsyll=None, makecesure=True):
    """
    Vérifie les comptes obtenus (potentiellement plusieurs en fonction des diérèses).
    """
    if nbsyll is None:
        return None
    oknbsyll = False
    for p in counts:
        if makecesure and nbsyll % 2 == 0:
            if p[-1] == nbsyll:
                oknbsyll = True
                if (nbsyll // 2) in p:
                    i = p.index(nbsyll // 2)
                    # pour que ce soit vraiment un parfait alexandrin
                    if not lexitems[i]["syllmuette"]:
                        return None
    if oknbsyll:
        return CESURE
    return NBSYLL

