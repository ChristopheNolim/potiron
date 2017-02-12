"""
@file mutators.py

Les mutateurs sont l'intérêt principal de Potiron. (Le concept fameux, comme
le nom, sont empruntés à un blog fort intéressant dont j'ai malheureusement
perdu l'adresse. Si vous la retrouvez merci de me l'indiquer !)

"""

from lexicon.rootmutator import RootMutator
from tagger.formatter import format_out
import random

class SelectiveMutator(RootMutator):
    """
    @class SelectiveMutator

    Mutateur qui ne mute que les adjectifs, verbes, noms et adverbes.
    """

    def __init__(self):
        super().__init__()


    def synonyms(self, d, endpron="", dom="", niv=""):
        if d["gram"] in ["ADJ", "VER", "NOM", "ADV"]:
            res = super().synonyms(d, endpron, dom, niv)
            random.shuffle(res)
            return [d] if not res else res
        else:
            return [d]

    def mutations(self, d, endpron="", dom="", niv=""):
        if d["gram"] in ["ADJ", "VER", "NOM", "ADV"]:
            tmp = super().mutations(d, endpron, dom, niv)
            random.shuffle(tmp)
            return tmp
        else:
            return [d]


class SynonymsMutator(SelectiveMutator):
    """
    @SynonymsMutator

    Mutateur qui mute par synonymes.
    """

    def __init__(self):
        super().__init__()

    def mutation_choices(self, tagged_sent):
        """
        Returns a list of choices (new possible words, not dicts) for each tagged word
        in this sentence (possibly more than a sentence).
        """
        return [ [c["orth"] for c in self.synonyms(t)] for t in tagged_sent]

    def mutation_sent(self, tagged_sent):
        possib = []
        for t in tagged_sent:
            possib.append(self.synonyms(t))
        return format_out( [random.choice(c)["orth"] for c in possib] )


class SameDomMutator(SelectiveMutator):

    def __init__(self):
        super().__init__()

    def mutation_choices(self, tagged_sent):
        """
        Returns a list of choices (new possible words, not dicts) for each tagged word
        in this sentence (possibly more than a sentence).
        """
        return [ [c["orth"] for c in self.mutations(t, endpron="", dom=t["dom"], niv="")] for t in tagged_sent]

    def mutation_sent(self, tagged_sent):
        possib = []
        for t in tagged_sent:
            possib.append(self.mutations(t, endpron="", dom=t["dom"], niv=""))
        return format_out( [random.choice(c)["orth"] for c in possib] )


class DefaultDomMutator(SelectiveMutator):
    """
    @class DefaultDomMutator

    Mutateur qui mute vers un nouveau domaine.
    """

    def __init__(self):
        super().__init__()

    def mutations(self, tmp, dom="", endpron=""):
        """
        Ne renvoie jamais un résultat vide.
        """
        # TODO
        if "|" in dom:
            # TODO améliorer le comportement
            choices = []
            for d in dom.split("|"):
                choices += super().mutations(tmp, dom=d, endpron=endpron)
        else:
            choices = super().mutations(tmp, endpron=endpron, dom=dom)

        # COL	couleurs
        # PSY	psychologie
        # FAC	façon, manière
        # LOC	locatif, lieux
        # LOQ	parole, parler
        if tmp["gram"] in ["ADJ"]:
            choices += super().mutations(tmp, dom="PSY", endpron=endpron)[:10] #+ super().mutations(tmp, dom="QUA", endpron=endpron)
        elif tmp["gram"] == "VER":
            choices += super().mutations(tmp, dom="LOQ", endpron=endpron)[:10] # + super().mutations(tmp, dom="LOQ", endpron=endpron)
        elif tmp["gram"] == "NOM":
            choices += super().mutations(tmp, dom="PSY", endpron=endpron)[:10] #+ super().mutations(tmp, dom="MUS", endpron=endpron) + super().mutations(tmp, dom="DRO", endpron=endpron)
        elif tmp["gram"] in ["ADV"]:
            choices += super().mutations(tmp, dom="PSY", endpron=endpron)[:10]
        else:
            choices = [tmp]
        return choices


class DomMutator(SelectiveMutator):
    """
    @class DomMutator

    UNUSED
    """

    def __init__(self):
        super().__init__()

    def mutations(self, tmp, dom="", endpron=""):
        # MUST NOT RETURN AN EMPTY RESULT
        # TODO
        # for k in ["pron", "genra", "nb", "typ", "dom", "niv", "temps", "pers", "more", "lemma"]:
        #     if k not in tmp:
        #         tmp[k] = ""
        if "|" in dom:
            # TODO améliorer le comportement
            res = []
            for d in dom.split("|"):
                # if d == "PHY":
                #     print([c["orth"] for c in self.mutations(tmp, dom=d, endpron=endpron)] )
                #     return
                res += super().mutations(tmp, dom=d, endpron=endpron)
            if not res:
                return [tmp]
            else:
                return res
        if tmp["gram"] in ["ADJ"]:
            choices = super().mutations(tmp, endpron=endpron, dom=dom)
            # if not choices or random.random() < 0.25:
            if len(choices) < 5:
                choices += super().mutations(tmp, dom="PSY", endpron=endpron) + super().mutations(tmp, dom="QUA", endpron=endpron)
            return choices
        elif tmp["gram"] == "VER":
            choices = super().mutations(tmp, dom=dom, endpron=endpron)
            if len(choices) < 5:
            # if not choices or random.random() < 0.25:
                choices = super().mutations(tmp, dom="PSY", endpron=endpron) + super().mutations(tmp, dom="LOQ", endpron=endpron)
            return choices
        elif tmp["gram"] == "NOM":
            choices = super().mutations(tmp, dom=dom, endpron=endpron)# + mutator.mutations(tmp, dom="PSY") # + mutator.mutations(tmp, dom="HAB") + mutator.mutations(tmp, dom="MUS")
            if len(choices) < 5:
            # if not choices or random.random() < 0.1:
                choices += super().mutations(tmp, dom="PSY", endpron=endpron) + super().mutations(tmp, dom="MUS", endpron=endpron) + super().mutations(tmp, dom="DRO", endpron=endpron)
            return choices
        elif tmp["gram"] in ["ADV"]:
            choices = super().mutations(tmp, dom=dom, endpron=endpron)
            return choices
        else:
            return [tmp]
