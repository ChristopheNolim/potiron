"""
@file poemwriters.py


Contient des classes qui écrivent des poèmes avec une structure plus précise.

"""

from mutators.writers import PoemWriter


import random

# DOMS = list()
#
# with open("mutators/doms.txt") as f:
#     for line in f:
#         dom = line.split("\t")[0].rstrip().lstrip()
#         if dom.isupper():
#             DOMS.append(dom)

class SonnetWriter(PoemWriter):
    """
    @class SonnetWriter

    Écrit des sonnets.

    Usage :

    s = SonnetWriter(maindom="MAT")
    s.write_save()
    """

    def __init__(self, maindom="PHY"):
        super().__init__(strophepat=["AABB", "CCDD", "EEFFGG"],
                        domspat=[[maindom, maindom, maindom, maindom], [maindom, maindom, maindom, maindom], [maindom, maindom, maindom, maindom, maindom, maindom]],
                        versepat=[[4], [4], [3,3]])

class QuatrainsWriter(PoemWriter):

    def __init__(self, nb=1, maindom="PHY"):
        super().__init__(strophepat=[random.choice(["ABAB", "AABB", "ABBA"]) for i in range(nb)],
                        domspat=[ [maindom for i in range(4)] for j in range(nb)],
                        versepat=[[4] for i in range(nb)])


class DistiqueWriter(PoemWriter):

    def __init__(self, maindom="MAT"):
        super().__init__(strophepat=["AA"],
                        domspat=[[maindom, maindom]],
                        versepat=[[2]])
