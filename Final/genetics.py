import random

def custom_sort_key(char):
    return (char.lower(), 0 if char.isupper() else 1)

def sort_string_custom(s):
    return ''.join(sorted(s, key=custom_sort_key))

class Genotype:
    def __init__(self, paternalSet, maternalSet, mutationChance = 0.01):
        self.paternalSet = paternalSet
        self.maternalSet = maternalSet
        self.mutationChance = mutationChance

    def meiosis(self, crossingOverChance = 0.10, mutationChance = 0.01):
        newSet = []
        crossingOverChance = crossingOverChance
        for i in range(len(self.paternalSet)):
            if random.random() < 0.5:
                newChromosome = []
                for j in range(len(self.paternalSet[i].genes)):
                    newGene = []
                    for k in range(len(self.paternalSet[i].genes[j].alleles)):
                        rand = random.random()
                        if rand < mutationChance:
                            newGene.append(self.maternalSet[i].genes[j].alleles[k].swapcase())
                        elif rand < crossingOverChance:
                            newGene.append(self.paternalSet[i].genes[j].alleles[k])
                        else:
                            newGene.append(self.maternalSet[i].genes[j].alleles[k])
                    gen = Gene(newGene)
                    newChromosome.append(gen)
                chrom = Chromosome(newChromosome)
                newSet.append(chrom)
            else:
                newChromosome = []
                for j in range(len(self.maternalSet[i].genes)):
                    newGene = []
                    for k in range(len(self.maternalSet[i].genes[j].alleles)):
                        rand = random.random()
                        if rand < mutationChance:
                            newGene.append(self.paternalSet[i].genes[j].alleles[k].swapcase())
                        elif rand < crossingOverChance:
                            newGene.append(self.maternalSet[i].genes[j].alleles[k])
                        else:
                            newGene.append(self.paternalSet[i].genes[j].alleles[k])
                    gen = Gene(newGene)
                    newChromosome.append(gen)
                chrom = Chromosome(newChromosome)
                newSet.append(chrom)
        string = ""
        for i in range(len(newSet)):
            string += (repr(newSet[i]))
        #print(string)
        return newSet

    def __repr__(self):
        string = ""
        for i in range(len(self.paternalSet)):
            string += (repr(self.paternalSet[i]) + repr(self.maternalSet[i]))
        return string #sort_string_custom(string)
        

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