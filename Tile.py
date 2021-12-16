#
# Tile
#
# December 16th, 2021
#
# Class definition for a tile.
#

from Tools import Direction


class Tile:
    def __init__(self, symbol, color, glues, warnings=False) -> None:
        self.symbol = symbol
        self.color = color
        self.glues = glues

        # check if all glues are defined
        if glues.get(Direction.NORTH) == None and warnings:
            print(
                f"[bold yellow]WARNING[/bold yellow]: North glue is not defined for tile {self.symbol}")
        if glues.get(Direction.EAST) == None and warnings:
            print(
                f"[bold yellow]WARNING[/bold yellow]: East glue is not defined for tile {self.symbol}")
        if glues.get(Direction.SOUTH) == None and warnings:
            print(
                f"[bold yellow]WARNING[/bold yellow]: South glue is not defined for tile {self.symbol}")
        if glues.get(Direction.WEST) == None and warnings:
            print(
                f"[bold yellow]WARNING[/bold yellow]: West glue is not defined for tile {self.symbol}")

    def __str__(self) -> str:
        return f"symbol = {self.symbol} : color = {self.color} : glues = {self.glues}"
