"""
@file src/test.py
@version 1.0
@author CN
@author Gudule
@date fev 2017

Contient quelques tests (et du bordel).

"""


from tagger.tagger import Tagger
from verses import is_alexandrin
from mutators.formatter import format_tagged


text = """
Je servais à regret ses desseins amoureux ;
mais le sort irrité nous aveuglait tous deux.
le tyran m'a surpris sans défense et sans armes.
j'ai vu Pirithoüs, triste objet de mes larmes,
livré par ce barbare à des monstres cruels
qu'il nourrissait du sang des malheureux mortels.
moi-même il m'enferma dans des cavernes sombres,
lieux profonds et voisins de l'empire des ombres.
"""

text2 = """
Le tigre en sa caverne et la taupe en son trou
Disaient depuis longtemps: l'homme commettait des crimes.
Une mouche noire montait aux cieux sublimes,
Issue des flots épais des sombres actions.
Depuis longtemps l'azur perdait ses purs rayons,
Et perdait de nombreuses, hideuses toiles,
Où l'araignée humaine avait pris les étoiles.
"""

markov = {
"AST" : ["MUS", "OCE", "PHY", "GEL", "TPS"],
"OCE" : ["PIS", "CRU", "HYD", "MAR"],
"PHY" : ["MAT"],
"MYT" : ["ARM", "OCC", "REL", "GRE"],
"ARM" : ["FOR", "MIL"],
"ANI" : ["AVI", "BOT", "CHS", "CRU", "PIS", "REP", "ENT"],
"PLA" : ["BOT"],
"OBJ" : ["COL"],
"HIS" : ["PHS", "CUL", "ECR", "GEG"],
"ECR" : ["LITT", "LIN"]
}

t = Tagger()

tmp = t.tag(" une conception affectée oubliait un scorpion,")
tmp2 = format_tagged(tmp)
# for truc in tmp2:
#     print(truc)

print(is_alexandrin(tmp2, verbose=True))

t.close()

