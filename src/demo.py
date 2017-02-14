"""
@file src/demo.py
@version 1.0
@author CN
@author Gudule
@date fev 2017

Démo de Potiron.

"""


# from mutators.mutators import SynonymsMutator, SameDomMutator, DefaultDomMutator

#
# s = SonnetWriter(maindom="MOB")
# s.write_save()

# s = DistiqueWriter(maindom="MAT")
# s.write_save()

# s = QuatrainsWriter(maindom="AST", nb=3)
# s.write_save()

help_string = """
Bienvenue dans la démo de Potiron version 1.0 !
Pour le moment son usage est très simple :
- lancez demo.py en ligne de commande avec les arguments suivants :
- "sonnet DOM" pour écrire un sonnet sur le thème DOM et l'enregistrer
 automatiquement dans un dossier poemes/
 DOM doit être un des domaines du DEM dont la liste est fournie dans doms.txt
- "sonnet random" pour écrire un sonnet sur un thème aléatoire et l'enregistrer
 automatiquement dans un dossier poemes/
- "help" pour afficher cette aide.

Attention, selon les domaines, Potiron peut prendre plus de temps
et ne pas renvoyer de résultat. Plus d'informations dans le README.

"""

import sys

def display_help():
    print(help_string)

if __name__ == "__main__":

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg.endswith("help"):
            display_help()
            sys.exit()
    elif len(sys.argv) == 3:
        if sys.argv[1] != "sonnet":
            print("Je ne comprends pas la commande %s en entrée !" % sys.argv[1])
            sys.exit()
        else:
            from mutators.poemwriters import DistiqueWriter, SonnetWriter, QuatrainsWriter
            import random

            DOMS = list()

            with open("doms.txt") as f:
                for line in f:
                    dom = line.split("\t")[0].rstrip().lstrip()
                    if dom.isupper():
                        DOMS.append(dom)

            if sys.argv[2] == "random":
                dom = random.choice(DOMS)
                print("Le domaine choisi est %s" % dom)
            else:
                dom = sys.argv[2]

            if dom not in DOMS:
                print("%s n'est pas un domaine reconnu !" % dom)
            else:
                s = SonnetWriter(maindom=dom)
                s.write_save()

