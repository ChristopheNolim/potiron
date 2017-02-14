"""
@file src/update_structs.py
@version 1.0
@author CN
@author Gudule
@date fev 2017

"""

from mutators.structurator import Structurator


s = Structurator()
s.write_lists()

# check
s.load()

print(s.produce_alexs(1))


