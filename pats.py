import random
import copy


class ATAM:

    def __init__(self, gene):
        # gene is a length 978 array containing values from 0-18
        self.gene = gene
        self.bottomRow = copy.copy(gene[0:6])
        self.assembly = [[-1 for _ in range(4)] for __ in range(4)]
        self.prevEastGlue = gene[2]

        for i in range(4):
            self.assembly[0][i] = "S"
            self.assembly[i][0] = "S"


        self.glueDict = [[None for y in range(9)] for x in range(9)]

        self.tile_set = set()




    def terminal(self):

        for y in range(1,4):
            for x in range(1,4):
                
                northGlueInd = 6 + self.bottomRow[x] *(9*2) + (self.prevEastGlue) * 2
                northGlue = self.gene[northGlueInd]
                eastGlue = self.gene[northGlueInd+1]
    
                self.assembly[x][y] = (northGlue, eastGlue,self.bottomRow[x], self.prevEastGlue)
                self.tile_set.add(self.assembly[x][y])
                self.bottomRow[x] = northGlue
                self.prevEastGlue = eastGlue

        return self.assembly

    def print_assembly(self):
        print("Assembly:")
        for y in range(3,-1,-1):
            for x in range(4):
                print(str(self.assembly[x][y]).rjust(16),end="")
            print("")


    def tile_set_size(self):
        return len(self.tile_set)



def fitness(sys, pattern):
    print("a")






def generate_random_gene():
    gene = [0,1,2,3,4,5] + [0 for _ in range(972)]

    for x in range(6,972,2):
        gene[x] = random.randrange(9)
        gene[x+1] = random.randrange(9)

    return gene 


gene = generate_random_gene()
sys = ATAM(gene)
sys.terminal()
sys.print_assembly()
print("Size: ", sys.tile_set_size())


pattern = ()




while True:
    gene = generate_random_gene()
    sys = ATAM(gene)
    sys.terminal()

    if sys.tile_set_size() < 4:
        sys.print_assembly()
        print("Size: ", sys.tile_set_size())
        break
