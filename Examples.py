#
# Examples
#
# December 16th, 2021
#
# Some example code and objects.
#

from TilesetOrganism import TileGene, GlueGene, TilesetOrganism
from Tile import Tile
from Tools import Direction

# simplePattern builds the following
#
# b w
# b w
#


def simplePattern():
    org = TilesetOrganism()

    org.tileGenes.append(TileGene(1, "black"))
    org.tileGenes.append(TileGene(2, "white"))
    org.tileGenes.append(TileGene(3, "black"))
    org.tileGenes.append(TileGene(4, "white"))

    org.glueGenes.append(GlueGene(1, Direction.NORTH, 4))
    org.glueGenes.append(GlueGene(1, Direction.EAST, 3))
    org.glueGenes.append(GlueGene(1, Direction.SOUTH, 2))
    org.glueGenes.append(GlueGene(1, Direction.WEST, 1))

    org.glueGenes.append(GlueGene(2, Direction.NORTH, 4))
    org.glueGenes.append(GlueGene(2, Direction.EAST, 3))
    org.glueGenes.append(GlueGene(2, Direction.SOUTH, 2))
    org.glueGenes.append(GlueGene(2, Direction.WEST, 3))

    org.glueGenes.append(GlueGene(3, Direction.NORTH, 4))
    org.glueGenes.append(GlueGene(3, Direction.EAST, 3))
    org.glueGenes.append(GlueGene(3, Direction.SOUTH, 4))
    org.glueGenes.append(GlueGene(3, Direction.WEST, 1))

    org.glueGenes.append(GlueGene(4, Direction.NORTH, 4))
    org.glueGenes.append(GlueGene(4, Direction.EAST, 3))
    org.glueGenes.append(GlueGene(4, Direction.SOUTH, 4))
    org.glueGenes.append(GlueGene(4, Direction.WEST, 3))

    return org


def simplePatternSeed():
    seed = []
    seed.append([])
    seed.append([])
    seed.append([])

    # fill left column
    seed[0].append(Tile(0, 'white', {Direction.EAST: 1}))
    seed[1].append(Tile(0, 'white', {Direction.EAST: 1}))
    seed[2].append(Tile(0, 'white', {}))

    # fill bottom row
    seed[2].append(Tile(0, 'white', {Direction.NORTH: 2}))
    seed[2].append(Tile(0, 'white', {Direction.NORTH: 2}))

    return seed
