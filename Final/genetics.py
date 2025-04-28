import random

class Genotype:
    def __init__(self, paternalSet, maternalSet, mutationChance = 0.01):
        self.paternalSet = paternalSet
        self.maternalSet = maternalSet
        self.mutationChance = mutationChance

    def meiosis(self):
        newSet = []
        for i in len(self.paternalSet):
            if random.random() < 0.5:
                newChromosome = self.paternalSet[i]
            else:
                newChromosome = self.maternalSet[i]

    def __repr__(self):
        string = ""
        for pair in self.chromosomePairs:
            string += f"[{pair[0]}|{pair[1]}] "
        return string.strip()

class Chromosome:
    def __init__(self, list):
        self.genes = list

    def __repr__(self):
        return ''.join(repr(gene) for gene in self.genes)

class Gene:
    def __init__(self, list):
        self.alleles = list

    def __repr__(self):
        return ''.join(self.alleles)
