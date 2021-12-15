#
# Pattycake
#
# December 15th, 2021
#
# Runner file for Pattycake.
#

from TilesetOrganism import TileGene, GlueGene, Direction, TilesetOrganism

print("Genome Testing")
print()

org = TilesetOrganism()
org.tileGenes.append(TileGene(1, "black"))
org.tileGenes.append(TileGene(2, "white"))
org.glueGenes.append(GlueGene(1, Direction.NORTH, 1))
org.glueGenes.append(GlueGene(1, Direction.SOUTH, 1))
org.glueGenes.append(GlueGene(2, Direction.NORTH, 2))
org.glueGenes.append(GlueGene(2, Direction.SOUTH, 1))

print(org)
