"""
@file src/mutators/structurator.py
@version 1.0
@author CN
@author Gudule
@date fev 2017

Chargé de créér des structures d'alexandrins.

Le structurateur charge les structures depuis le fichier structures.txt.

"""

try:
    _TAGGER = True
    from tagger.tagger import Tagger
except ImportError as e:
    _TAGGER = False

from lexicon.lexiconitem import LexiconItem
from mutators.structurator_data import POSSIB, LISTS
import json
import random
import os



_VIRG = {'pron': '', 'dom': '', 'niv': '', 'gram': 'PUN', 'more': '', 'genra': '',
        'aux': '', 'orth': ',', 'temps': '', 'typ': '', 'nb': '', 'lemma': '', 'pers': ''}
_POINT = {'pron': '', 'dom': '', 'niv': '', 'gram': 'SEN', 'more': '', 'genra': '',
        'aux': '', 'orth': '.', 'temps': '', 'typ': '', 'nb': '', 'lemma': '', 'pers': ''}

_VIRG = LexiconItem.from_dict(_VIRG)
_POINT = LexiconItem.from_dict(_POINT)

#==============================================================================

class Structurator:
    """
    @class Structurator

    Le structurateur a trois capacités principales :
    * charger le fichier de structures "structure.txt"
    * écrire le fichier de structures "structure.txt"
    (il a besoin pour ce faire d'accéder à un tagger, fonctionnalité qui
    n'est pour l'instant pas distribuée avec Potiron).
    * générer des structures grammaticalement correctes, alexandrin
    par alexandrin.

    """

    def __init__(self):
        """
        Initialise le structurateur (donc ne fait rien de spécial).
        """
        self.d = dict()

    def load(self):
        """
        Charge le fichier structures.txt.
        """
        print("Structurator : Loading")
        currentdir = os.path.dirname(os.path.abspath(__file__))
        fname = os.path.join(currentdir, "structures.txt")
        with open(fname, "r") as f:
            for l in f:
                i, t = json.loads(l)
                self.d[i] = [[LexiconItem.from_dict(v) for v in u] for u in t]
        print("Structurator : Done loading")

    def write_lists(self):
        """
        Écrit les listes de structures dans structures.txt.
        Pour ce faire, un tagger est nécessaire.
        """
        if not _TAGGER:
            print("Structurator : impossible d'écrire les listes. Pas de Tagger.")
            return

        print("Structurator : Writing lists...")
        t = Tagger()
        currentdir = os.path.dirname(os.path.abspath(__file__))
        fname = os.path.join(currentdir, "structures.txt")
        # TODO : tagguer par liste (plus rapide)
        with open(fname, "w") as f:
            for i in LISTS:
                tagged = t.tag_list(LISTS[i])
                s = (i, [[v.dismiss_non_grammar(ex=["pourquoi", "ainsi", "dans", "tels", "tel", "comme", "qui"]).to_dict() for v in u] for u in tagged])
                # s = (i, [[v.dismiss_non_grammar(ex=["pourquoi", "ainsi", "dans", "tels", "tel", "comme", "qui"]).to_dict() for v in t.tag(u)] for u in LISTS[i]])
                f.write(json.dumps(s) + "\n")
        t.close()
        print("Structurator : Done writing !")

    def produce_alexs(self, u):
        """
        Produit des alexandrins formant une ou des phrases correctes
        (ponctuation comprise).

        @param u    Nombre d'alexandrins à produire.
        """
        return self._get_alexs(u)

    def default_prod_alexs(self, u):
        """
        @todo retirer (non utilisé)
        """
        return [ random.choice(self.d[7]) + [_POINT] for i in range(u) ]

    def _get_alexs(self, nb):
        rtmp = []
        s = 0
        while s < nb:
            l = random.choice(POSSIB)
            if s + len(l) <= nb:
                rtmp.append(l)
                s += len(l)
        res = []
        for l in rtmp:
            for i in l[:-1]:
                res.append( random.choice(self.d[i]) + [_VIRG] )
            res.append ( random.choice(self.d[l[-1]]) + [_POINT] )
        return res
