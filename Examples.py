#
# Examples
#
# December 16th, 2021
#
# Some example code and objects.
#

from functools import WRAPPER_ASSIGNMENTS
from TilesetOrganism import TileGene, GlueGene, TilesetOrganism
from Tile import Tile
from Tools import Direction

# simplePattern builds the following
#
# b w
# b w
#


def simplePatternOrg():
    # read data from the file
    with open("organisms/simpleOrganism", "r") as f:
        lines = f.readlines()

    org = TilesetOrganism()
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
    # read data from the file
    with open("organisms/simpleSeed", "r") as f:
        lines = f.readlines()

    westGlues = lines[0].split()
    southGlues = lines[1].split()

    print(westGlues)
    print(southGlues)

    seed = []

    # add all the rows
    for i in range(len(westGlues) + 1):
        seed.append([])

    # fill left column
    for i in range(len(westGlues)):
        seed[i].append(Tile(0, 'w', {Direction.EAST: int(westGlues[i])}))

    # fill corner tile
    seed[len(westGlues)].append(Tile(0, 'w', {}))

    # fill bottom row
    for i in range(len(southGlues)):
        seed[len(southGlues)].append(Tile(0, 'w',
                                          {Direction.NORTH: int(southGlues[i])}))

    return seed
