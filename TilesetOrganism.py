#
# TilesetOrganism
#
# December 15th, 2021
#
# Class definitions for a genotype representing a tileset.
#

from enum import Enum


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


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
