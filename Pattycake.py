#
# Pattycake
#
# December 16th, 2021
#
# Runner file for Pattycake.
#

from Assembly import Assembly
from Examples import simplePatternOrg
from rich import print

print("Genome Testing")
print()

org = simplePatternOrg()
print(org)

tileset = org.tileset()
assembly = Assembly(tileset)
assembly.assemble(True)

print("final assembly")
assembly.showAssembly()
