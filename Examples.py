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

    with open("organisms/simple") as f:
        lines = f.readlines()

    for l in lines:
        tokens = l.split()

        # should be 1 symbol, 1 color, 4 directions
        if len(tokens) != 6:
            continue

        symbol = int(tokens[0])
        color = tokens[1]
        n = int(tokens[2])
        e = int(tokens[3])
        s = int(tokens[4])
        w = int(tokens[5])

        org.tileGenes.append(TileGene(symbol, color))
        org.glueGenes.append(GlueGene(symbol, Direction.NORTH, n))
        org.glueGenes.append(GlueGene(symbol, Direction.EAST, e))
        org.glueGenes.append(GlueGene(symbol, Direction.SOUTH, s))
        org.glueGenes.append(GlueGene(symbol, Direction.WEST, w))

    return org


def simplePatternSeed():
    seed = []
    seed.append([])
    seed.append([])
    seed.append([])

    # fill left column
    seed[0].append(Tile(0, 'w', {Direction.EAST: 1}))
    seed[1].append(Tile(0, 'w', {Direction.EAST: 1}))
    seed[2].append(Tile(0, 'w', {}))

    # fill bottom row
    seed[2].append(Tile(0, 'w', {Direction.NORTH: 2}))
    seed[2].append(Tile(0, 'w', {Direction.NORTH: 2}))

    return seed
