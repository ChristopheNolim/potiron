
"""
@file src/mutators/writers.py
@version 1.0
@author CN
@author Gudule
@date fev 2017

Ce fichier contient les classes principales chargées d'écrire des poèmes.

"""

from mutators.mutators import DefaultDomMutator
import random
from mutators.formatter import format_out, format_tagged
from verses import is_alexandrin
from mutators.structurator import Structurator
import time
import os


class StropheWriter2:
    """
    @class StropheWriter2

    Écrit une belle strophe.
    Il y a beaucoup de code magique dans cette classe.
    """

    def __init__(self, mutator):
        self.m = mutator

    def set_pattern(self, pat, domspat):
        """
        Ajoute le pattern des vers et le pattern de domaines.
        Un vers = un domaine pour l'instant.

        @param pat  pattern de vers. AA ou ABBA par ex.
                    Chaque terminaison correspond à une lettre.
        @param domspat  Pattern de domaines. À chaque vers un domaine.
        """
        self.pattern = pat
        self._dict = dict()
        for i in range(len(self.pattern)):
            if self.pattern[i] not in self._dict:
                self._dict[self.pattern[i]] = [i]
            else:
                self._dict[self.pattern[i]].append(i)
        self.doms = domspat
        # à la fin la variable interne _dict contient, pour chaque lettre
        # différente dans le pattern, la liste des vers (index de chaque)
        # qui doivent se terminer de la même façon
        if len(self.pattern) != len(self.doms):
            raise Exception("Bad use of StropheWriter !")

    def set_tags_pat(self, tagspat):
        """
        Ajoute le pattern de mots prévus pour cette strophe.
        Conséquemment, envoie toutes les requêtes idoines au mutator (afin
        de ne pas avoir à les refaire plus tard).

        @param tagspat doit être une liste de listes de tags (les vers eux-mêmes).
        """

        if len(tagspat) != len(self.pattern):
            raise Exception("Provided a bad pattern of tags")
        self.tagspat = tagspat
        self.choices = [ [self.m.mutations(t, dom=self.doms[i]) for t in tagspat[i]] for i in range(len(tagspat)) ]
        # self.choices stocke tous les choix possibles
        # retrouve ensuite les positions des derniers mots de chaque vers
        # (oublie la ponctuation en fin de vers)
        lastpos = [ 0 for l in tagspat]
        for j in range(len(tagspat)):
            for i in range(len(tagspat[j])):
                if tagspat[j][i]["gram"] not in ["PUN", "SEN"]:
                    lastpos[j] = i
        self.lastpos = lastpos
        # trouve toutes les fins de vers possibles
        self.possibends = [ self.choices[i][lastpos[i]] for i in range(len(tagspat))]

        # la suite du calcul dans write_strophe...

    def write_strophe(self, trials=1):

        if trials > 1:
            res = self.write_strophe(trials-1)
            if res:
                return res

        finalends = [ None for i in range(len(self.tagspat)) ]
        # choices = list(self.choices) # copie

        # mixe un peu le tout
        for l in self.possibends:
            random.shuffle(l)

        lemmas = list()
        for c in self._dict:
            l = self._dict[c]
            found = False
            current = ""
            # trouve le premier indice de vers qui doit avoir cette terminaison
            first = l[0]
            j = 0
            while j < len(self.possibends[first]) and not found:
                # parcourt tous les mots possibles pour cette terminaison de vers
                p = self.possibends[first][j]
                # regarde la pron
                current = p["pron"][-2:]
                finalends[first] = p
                lemmas = [p["lemma"]]
                for i in l[1:]:
                    finalends[i] = None
                    k = 0
                    found2 = False
                    while k < len(self.possibends[i]) and not found2:
                        n = self.possibends[i][k]
                        if n["pron"][-2:] == current:
                            if len(list(set( lemmas + [n["lemma"]] ))) == len(lemmas) + 1:
                                lemmas.append(n["lemma"])
                                finalends[i] = n
                                found2 = True
                        k += 1
                found = True
                for i in l[1:]:
                    if finalends[i] is None: # un vers qui manque
                        found = False

                j += 1
            # si on n'a pas trouvé de possibilité de rimes, c'est vraiment pas de bol
            if not found:
                return []

        # à ce point, lemmas contient les lemmas des mots finaux
        # print(finalends)

        # les contraintes e non-répétition s'accumulent linéairement !
        res = []

        lemmas = list() # la non-répétition va être revérifiée
        for j in range(len(self.tagspat)):
            trials = 0
            found = False
            while trials < 50 and not found:
                trials += 1
                # faire un choix
                choice = [ random.choice(truc) for truc in self.choices[j] ]
                # ajouter la contrainte du dernier mot
                choice[self.lastpos[j]] = finalends[j]
                # calculer tous les nouveaux lemmes
                newlemmas = [c["lemma"] for c in choice if c["lemma"] != "" and c["gram"] in ["VER", "ADJ", "NOM", "ADV"]]

                if len(list(set(lemmas + newlemmas))) == len(lemmas + newlemmas):
                    # possib = format_out([ truc["orth"] for truc in choice ])
                    tmp = format_tagged(choice)
                    if is_alexandrin(tmp):
                        found = True
                        possib = format_out([ truc["orth"] for truc in tmp ])
                        res.append(possib)
                        lemmas = lemmas + newlemmas

            if not found:
                return []

        return res


#=============================================================================


class PoemWriter:
    """
    @class PoemWriter

    Classe qui écrit un bô poème.
    """

    def __init__(self, strophepat, domspat, versepat):
        # TODO check patterns !
        self.struct = Structurator()
        self.struct.load()
        self.m = DefaultDomMutator()
        self.strophes = StropheWriter2(self.m)
        # self.doms = doms
        # self.maindom = doms[0]
        self.strophepat = strophepat
        self.domspat = domspat
        self.versepat = versepat


    def write(self, maxtrials=10):
        res = []
        for i in range(len(self.strophepat)):
            j = 0
            ok = False
            while not ok and j < maxtrials:
                j += 1
                # try:
                st = [] # modèle de la strophe ou du couple de strophes
                for u in self.versepat[i]:
                    st += self.struct.produce_alexs(u)
                self.strophes.set_pattern(self.strophepat[i], self.domspat[i])
                self.strophes.set_tags_pat(st)
                tmp = self.strophes.write_strophe(trials=20)
                if tmp:
                    print("Une nouvelle strophe OK")
                    ok = True
                    k = 0
                    l = []
                    counter = 0
                    for c in self.versepat[i]:
                        counter += c
                        l.append((counter - c, counter))
                    for c in l:
                        res += tmp[c[0]:c[1]]
                        res.append("\n") # changement de strophe
                if j % 10 == 0:
                    print("J'ai fait %i essais, le maximum est %i" % (j, maxtrials))
                # except Exception as e:
                #     pass
            if not ok:
                return

        self.m.close()
        return res

    def write_save(self, maxtrials=100):
        """
        Écrit le poème et le sauvegarde dans un nouveau fichier.
        """
        l = self.write(maxtrials)
        if l:
            srcdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            dirname = os.path.join(srcdir, "poems")
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fname = "%s.txt" % (str(time.strftime("%d-%m-%y-%H:%M:%S")))
            with open(os.path.join(dirname, fname), "w") as f:
                for u in l:
                    f.write(u + "\n")
                    print(u)
                print("Le poème a été sauvegardé dans le fichier %s" % fname)

