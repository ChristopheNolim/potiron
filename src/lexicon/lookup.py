"""
@file src/lexicon/lookup.py
@version 1.0
@author CN
@author Gudule
@date fev 2017

Utilisé uniquement lorsqu'on parse un texte en entrée, donc
lorsque l'on taggue.

Interroge la DB.

@todo le lexique ne gère pas pour l'instant les verbes composites.
"""

import sqlite3
from lexicon.lexiconitem import LexiconItem
import os


_COMPOSES2 = {
"PRE" : "PCOMP",
"IMP" : "PQP",
"PSIMP" : "PANT",
"FSIMP" : "FANT",
"SPRE" : "SPAS",
"SIMP" : "SPQP",
"IMPPRE" : "IMPPAS",
"CONDPRE" : "CONDPAS1",
"PPRE" : "PASSIPPRE",
"INF" : "PASSIFINF"
}


class LexiconLooker:
    """
    @class LexiconLooker

    Encapsule une connexion à la base de données sous-jacente.
    """

    def __init__(self):
        currentdir = os.path.dirname(os.path.abspath(__file__))
        fname = os.path.join(currentdir, 'lexicon/lexique.db')
        self.conn = sqlite3.connect(fname)

    def close(self):
        self.conn.close()

    def exists(self, word, gram):
        """
        Cherche si un tel mot (avec cette fonction grammaticale) existe dans le lexique.
        """
        tmp = self.conn.execute(
            """SELECT * from lexique WHERE (gram=? AND orth=?)""", (gram, word))
        if tmp:
            return True
        return False

    def lookup(self, word, gram):
        if " " in word and gram == "VER:COMP":
            # TODO
            # print("Warning : composite vbs currently not handled")
            # return LexiconItem.from_word_gram(word, gram)
            l = word.split(" ")
            if len(l) == 2:
                tmp1 = self.lookup(l[0], "VER")
                tmp2 = self.lookup(l[1], "VER")
                if (tmp1["lemma"] in ["avoir", "être"]
                    and tmp2["gram"] == "VER" # verbe confirmé
                    and tmp2["aux"] == tmp1["lemma"] # bon auxiliaire
                    ):
                    if tmp1["temps"] in _COMPOSES2:
                        tmp2["temps"] = _COMPOSES2[tmp1["temps"]]
                        tmp2["nb"] = tmp1["nb"]
                        tmp2["pers"] = tmp1["pers"]
                        return tmp2
            return LexiconItem.from_word_gram(word, gram)

        tmp = self.conn.execute(
            """SELECT * from lexique WHERE (gram=? AND orth=?)""", (gram, word))
        if tmp:
            for r in tmp:
                return LexiconItem.from_entry(r)

        return LexiconItem.from_word_gram(word, gram)

