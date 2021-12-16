#
# Assembly
#
# December 16th, 2021
#
# Class definitions for an aTAM simulator.
#

from Examples import simplePatternSeed
from Tile import Tile
from Tools import Direction
from rich import print
from rich.console import Console
console = Console()


class Assembly:
    def __init__(self, tileset) -> None:
        self.tileset = tileset

        # to store the assembly
        self.tiles = []

        # to store the locations for new tiles
        self.open = []

    def __str__(self) -> str:
        if len(self.tiles) == 0:
            return "Empty Assembly"

        res = ""

        for row in self.tiles:

            t: Tile
            for t in row:
                res += str(t.symbol) + " "
            res += "\n"

        return res

    def showAssembly(self) -> None:
        if len(self.tiles) == 0:
            return

        currRow = 0
        goalRow = int(len(self.tiles) / 2)

        for row in self.tiles:
            # row prefix
            if currRow == goalRow:
                console.print(" A = ", end="")
            else:
                console.print("     ", end="")

            t: Tile
            for t in row:
                if t.symbol == 0:
                    console.print(" S ", end="", style="#ffffff on #555555")
                elif t.color == "b":
                    console.print("   ", end="", style="#ffffff on #000000")
                else:
                    console.print("   ", end="", style="#000000 on #bbbbbb")

            console.print()
            currRow += 1

        console.print()

    def isTaken(self, x, y) -> bool:
        # check bounds first
        if x < 0 or x >= len(self.tiles):
            return False

        if y < 0 or y >= len(self.tiles[x]):
            return False

        return Tile

    def assemble(self, debug=False) -> None:
        # get seed
        self.tiles = simplePatternSeed()

        # set initial open location
        self.open.append((1, 1))

        if debug:
            self.showAssembly()
            print("open spots")
            print(self.open)
            print()

        # simulate
        while len(self.open) != 0:
            # grab an element off the front
            x, y = self.open.pop()

            if debug:
                print(f"Trying to fill {x=} {y=}")
                print()

            # found out glue types that need to match
            southGlue = self.tiles[x + 1][y].glues[Direction.NORTH]
            westGlue = self.tiles[x][y - 1].glues[Direction.EAST]

            if debug:
                print("looking for matching glues for the following")
                print(f"{westGlue=}")
                print(f"{southGlue=}")
                print()

            # find matching tile
            t: Tile
            for t in self.tileset:
                if t.glues.get(Direction.SOUTH) == southGlue and t.glues.get(Direction.WEST) == westGlue:
                    # found a tile, place down
                    self.tiles[x].append(Tile(t.symbol, t.color, t.glues))

                    # update open spots
                    if self.isTaken(x + 1, y + 1):
                        self.open.append((x, y + 1))

                    if self.isTaken(x - 1, y - 1):
                        self.open.append((x - 1, y))

                    break

            if debug:
                self.showAssembly()
                print("open spots")
                print(self.open)
                print()
