"""
@file src/mutators/poemwriters.py
@version 1.0
@author CN
@author Gudule
@date fev 2017


Contient des classes qui écrivent des poèmes avec une structure plus précise.

"""

from mutators.writers import PoemWriter


import random



_QUATRAIN_PAT = ["AABB", "ABBA", "ABAB"]

_BISTROPHE_PAT = ["EEFFGG", "EFFEGG", "EFEFGG",
                "EEFGGF", "EEFGFG"]


class SonnetWriter(PoemWriter):
    """
    @class SonnetWriter

    Écrit des sonnets.

    Usage :

    s = SonnetWriter(maindom="MAT")
    s.write_save()
    """

    def __init__(self, maindom="PHY"):
        super().__init__(strophepat=[random.choice(_QUATRAIN_PAT), random.choice(_QUATRAIN_PAT), random.choice(_BISTROPHE_PAT)],
                        domspat=[[maindom, maindom, maindom, maindom], [maindom, maindom, maindom, maindom], [maindom, maindom, maindom, maindom, maindom, maindom]],
                        versepat=[[4], [4], [3,3]])

class QuatrainsWriter(PoemWriter):

    def __init__(self, nb=1, maindom="PHY"):
        super().__init__(strophepat=[random.choice(_QUATRAIN_PAT) for i in range(nb)],
                        domspat=[ [maindom for i in range(4)] for j in range(nb)],
                        versepat=[[4] for i in range(nb)])


class DistiqueWriter(PoemWriter):

    def __init__(self, maindom="MAT"):
        super().__init__(strophepat=["AA"],
                        domspat=[[maindom, maindom]],
                        versepat=[[2]])

