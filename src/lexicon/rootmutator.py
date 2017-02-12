"""
@file rootmutator.py

Ce fichier contient la racine de tous les mutateurs.
Il interroge la DB du lexique.

"""

import random
import sqlite3
from lexicon.lexiconitem import LexiconItem, addaux


class RootMutator:
    """
    @RootMutator

    Le mutateur contient une connexion à la DB.
    """

    def __init__(self):
        self.conn = sqlite3.connect('lexicon/lexique.db')

    def close(self):
        self.conn.close()

    def synonyms(self, d, endpron="", dom="", niv=""):
        """
        Mute par synonymes. Renvoie toujours au moins un résultat (le mot lui-même).
        S'il y a des mutations possibles, le mot ne fera pas partie du renvoi.
        """
        if type(d) != LexiconItem:
            raise TypeError("Wrong type")
        tmp1 = self.conn.execute("""SELECT * from thesaurus WHERE (lemma=? AND gram=?)""", (d["lemma"], d["gram"]) )
        if tmp1:
            for res in tmp1:
                syns = res[2].split("|")
                random.shuffle(syns)

                more = d["more"]
                pers = d["pers"]
                temps = d["temps"]
                nb = d["nb"]
                gram = d["gram"]
                genra = d["genra"]
                typ = "HUMAIN" if "HUMAIN" in d["typ"] else d["typ"]
                l = []
                for s in syns[:10]:
                    tmp = self.conn.execute(
                        """SELECT * from lexique WHERE (lemma=? AND gram=? AND genra=? AND tps=? AND pers=? AND nb=? AND typ LIKE ? AND dom LIKE ? AND niv LIKE ? AND pron LIKE ?)""",
                        (s, gram, genra, temps, pers, nb, '%' + typ + '%', '%' + dom + '%', '%' + niv + '%', '%' + endpron))
                    if tmp:
                        l += [res for res in tmp]
                if l:
                    return [LexiconItem.from_entry(t) for t in l]
                return [d]

        return [d]


    def mutations(self, d, endpron="", dom="", niv=""):
        """
        Fait muter un mot.
        Renvoie une liste de LexiconItem, jamais vide (si aucune mutation possible,
        le mot lui-même est renvoyé).

        @todo ne fonctionne pas pour les verbes à temps composés
        """

        # if d["temps"] in _COMPOSES:
        #     tmpdict = dict()
        #     tmpdict["temps"] = d["temps"]
        #     tmpdict["pers"] = d["pers"]
        #     tmpdict["nb"] = d["nb"]
        #     tpsaux = _COMPOSES[d["temps"]]
        #
        #     d["temps"] = "PPAS"
        #     d["pers"] = ""
        #     d["nb"] = ""
        #     l = self._mutations(d, endpron, dom, niv)
        #     # res = list()
        #     for tmp in l:
        #         addaux(tmp)
        #         conjaux = AUX[tmp["aux"]][tpsaux][tmpdict["nb"]][tmpdict["pers"]]
        #         tmp["temps"] = tmpdict["temps"]
        #         tmp["pers"] = tmpdict["pers"]
        #         tmp["nb"] = tmpdict["nb"]
        #         tmp["orth"] = conjaux + " " + tmp["orth"]
        #     return l

        return self._mutations(d, endpron, dom, niv)


    def _mutations(self, d, endpron="", dom="", niv=""):
        # TODO gérer les cas où plusieurs temps sont possibles ?????
        more = d["more"]
        pers = d["pers"]
        temps = d["temps"]
        nb = d["nb"]
        gram = d["gram"]
        genra = d["genra"]
        typ = "HUMAIN" if "HUMAIN" in d["typ"] else d["typ"]
        tmp = self.conn.execute(
            """SELECT * from lexique WHERE (gram=? AND genra=? AND tps LIKE ? AND pers=? AND nb=? AND typ LIKE ? AND dom LIKE ? AND niv LIKE ? AND pron LIKE ?)""",
            (gram, genra, '%' + temps + '%', pers, nb, '%' + typ + '%', '%' + dom + '%', '%' + niv + '%', '%' + endpron))
        if tmp:
            l = [res for res in tmp]
            if l:
                return [LexiconItem.from_entry(t) for t in l]
        return [d]


    def mutation(self, d, endpron="", dom="", niv=""):
        l = self.mutations(d, endpron, dom, niv) + [d]
        return l[random.randrange(len(l))]["orth"]



AUX = {"avoir" : {"PPRE": "ayant", "AUX": "avoir", "INF": "avoir", "PPAS": "eu",
"PRE" : {"s": {"1": "ai", "3": "a", "2": "as"}, "p": {"1": "avons", "3": "ont", "2": "avez"}},
"IMP" : {"s": {"1": "avais", "3": "avait", "2": "avais"}, "p": {"1": "avions", "3": "avaient", "2": "aviez"}},
"PSIMP" : {"s": {"1": "eus", "3": "eut", "2": "eus"}, "p": {"1": "eûmes", "3": "eurent", "2": "eûtes"}},
"FSIMP" : {"s": {"1": "aurai", "3": "aura", "2": "auras"}, "p": {"1": "aurons", "3": "auront", "2": "aurez"}},
"SPRE" : {"s": {"1": "aie", "3": "ait", "2": "aies"}, "p": {"1": "ayons", "3": "aient", "2": "ayez"}},
"SIMP" : {"s": {"1": "eusse", "3": "eût", "2": "eusses"}, "p": {"1": "eussions", "3": "eussent", "2": "eussiez"}},
"IMPPRE" : {"s": {"2": "aie"}, "p": {"1": "ayons", "2": "ayez"}},
"CONDPRE" : {"s": {"1": "aurais", "3": "aurait", "2": "aurais"}, "p": {"1": "aurions", "3": "auraient", "2": "auriez"}},
},
"être" : {"PPRE": "étant", "AUX": "avoir", "INF": "être", "PPAS": "été",
"PRE" : {"s": {"1": "suis", "3": "est", "2": "es"}, "p": {"1": "sommes", "3": "sont", "2": "êtes"}},
"IMP" : {"s": {"1": "étais", "3": "était", "2": "étais"}, "p": {"1": "étions", "3": "étaient", "2": "étiez"}},
"PSIMP" : {"s": {"1": "fus", "3": "fut", "2": "fus"}, "p": {"1": "fûmes", "3": "furent", "2": "fûtes"}},
"FSIMP" : {"s": {"1": "serai", "3": "sera", "2": "seras"}, "p": {"1": "serons", "3": "seront", "2": "serez"}},
"SPRE" : {"s": {"1": "sois", "3": "soit", "2": "sois"}, "p": {"1": "soyons", "3": "soient", "2": "soyez"}},
"SIMP" : {"s": {"1": "fusse", "3": "fût", "2": "fusses"}, "p": {"1": "fussions", "3": "fussent", "2": "fussiez"}},
"IMPPRE" : {"s": {"2": "sois"}, "p": {"1": "soyons", "2": "soyez"}},
"CONDPRE" : {"s": {"1": "serais", "3": "serait", "2": "serais"}, "p": {"1": "serions", "3": "seraient", "2": "seriez"}},
}
}

_COMPOSES = {
"PCOMP" : "PRE",
"PQP" : "IMP",
"PANT" : "PSIMP",
"FANT" : "FSIMP",
"SPAS" : "SPRE",
"SPQP" : "SIMP",
"IMPPAS" : "IMPPRE",
"CONDPAS1" : "CONDPRE",
"PASSIFINF" : "INF",
"PASSIPPRE" : "PPRE"
}
