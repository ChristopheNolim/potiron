"""
@file lexiconitem.py

Item de lexique.

"""

import json

_KEYS = ["orth", "gram", "pron", "genra", "nb", "typ", "dom", "niv", "temps", "pers", "more", "lemma", "aux"]
_NON_GRAM_KEYS = ["pron", "typ", "dom", "niv"] # pour l'instant laisser l'orthographe
# edit : je supprime aussi lemma

_AUXETRE = [
"aller", "arriver", "descendre", "redescendre",
"devenir", "redevenir", "entrer", "rentrer",
"mourir", "naître", "renaître", "partir", "repartir",
"retourner", "sortir", "ressortir", "tomber", "retomber",
"venir", "revenir", "parvenir", "survenir", "intervenir"
]

def addaux(d):
    if d["gram"] != "VER":
        return
    if d["lemma"] == "monter" or d["lemma"] == "remonter":
        if d["more"] == "INTR":
            d["aux"] = "être"
            return
    if d["lemma"] in _AUXETRE:
        d["aux"] = "être"
    d["aux"] = "avoir"

#=============================================================================

class LexiconItem:
    """
    @class LexiconItem

    Un item de lexique et les différentes méthodes pour le sauvegarder,
    le transformer en dictionnaire, etc.
    
    """

    def __init__(self):
        self._d = dict()

    def _input(self, d):
        for k in d:
            if k in _KEYS:
                self._d[k] = d[k]

    @staticmethod
    def from_word_gram(word, gram):
        n = LexiconItem()
        n["orth"] = word
        n["gram"] = gram
        return n

    @staticmethod
    def from_entry(entry):
        if type(entry) != tuple or len(entry) != 12:
            raise Exception("Bad entry provided !")
        orth, gram, lemma, pron, genra, nb, typ, dom, niv, temps, pers, more = entry
        d = dict()
        d["orth"] = orth
        d["gram"] = gram
        d["lemma"] = lemma
        d["pron"] = pron
        d["genra"] = genra
        d["nb"] = nb
        d["typ"] = typ
        d["dom"] = dom
        d["niv"] = niv
        d["temps"] = temps
        d["pers"] = pers
        d["more"] = more
        addaux(d)
        return LexiconItem.from_dict(d)

    @staticmethod
    def from_dict(d):
        n = LexiconItem()
        n._input(d)
        return n

    def __setitem__(self, k, v):
        if k in _KEYS:
            self._d[k] = v
        else:
            raise Exception("Bad key !")

    def __getitem__(self, k):
        if k in _KEYS:
            if k in self._d:
                return self._d[k]
            else:
                return ""
        else:
            raise Exception("Bad key !")

    def to_JSON(self):
        return json.dumps(self._d)

    @staticmethod
    def from_JSON(s):
        d = json.loads(s)
        n = LexiconItem()
        n._input(d)
        return n

    def to_dict(self):
        return self._d

    def dismiss_non_grammar(self, ex=[]):
        if self["orth"] in ex:
            return self
        if self["gram"] in ["ADV", "NOM", "ADJ", "VER"]:
            for k in _NON_GRAM_KEYS:
                if k in self._d:
                    del self._d[k]
        return self

    def __str__(self):
        return self._d.__str__()

    def __repr__(self):
        return self._d.__repr__()
