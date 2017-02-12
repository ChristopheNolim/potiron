"""
Utiliser ce script pour mettre à jour les structures (mutators/structures.txt)
"""

from mutators.structurator import Structurator


s = Structurator()
s.write_lists()

# check
s.load()

print(s.produce_alexs(1))
