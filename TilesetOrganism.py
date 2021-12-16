#
# TilesetOrganism
#
# December 16th, 2021
#
# Class definitions for a genotype representing a tileset.
#

from Tile import Tile

# typedef
Tileset = set[Tile]


class TileGene:
    def __init__(self, symbol, color) -> None:
        self.symbol = symbol
        self.color = color

    def __str__(self) -> str:
        return f"symbol = {self.symbol} : color = {self.color}"


class GlueGene:
    def __init__(self, symbol, direction, glue) -> None:
        self.symbol = symbol
        self.direction = direction
        self.glue = glue

    def __str__(self) -> str:
        return f"symbol = {self.symbol} : dir = {self.direction} : glue = {self.glue}"


class TilesetOrganism:
    def __init__(self) -> None:
        self.tileGenes = []
        self.glueGenes = []

    def __str__(self) -> str:
        tgStrings = []
        ggStrings = []

        for tg in self.tileGenes:
            tgStrings.append(str(tg))

        for gg in self.glueGenes:
            ggStrings.append(str(gg))

        res = "Genotype\n\n"
        res += "TileGenes\n" + " \n".join(tgStrings)
        res += "\n\n"
        res += "GlueGenes\n" + " \n".join(ggStrings)
        res += "\n"

        return res

    def tileset(self) -> Tileset:
        res: set
        res = set()

        tg: TileGene
        for tg in self.tileGenes:
            # get all data for a tile object
            symbol = tg.symbol
            color = tg.color
            glues = {}

            gg: GlueGene
            for gg in self.glueGenes:
                if gg.symbol == symbol:
                    glues[gg.direction] = gg.glue

            # create a tile, add it to res
            res.add(Tile(symbol, color, glues))

        return res
