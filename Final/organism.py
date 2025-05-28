from genetics import*
from vectors import Vec
from water import*
from food import*

import os
import matplotlib.pyplot as plt
import math

organisms = []
speeds = []
visions = []
totalBodySegments = []

totalOrganisms = []
avgSpeeds = []
avgVisions = []
avgBodySegments = []

dt = 0.0001

class Organism:
    def __init__(self, Genotype, position):
        self.pastPos = position
        self.pos = position
        self.nextPos = position
        self.Genotype = Genotype
        self.Phenotype = self.geneExpression()
        self.color = [self.Phenotype['r'], self.Phenotype['g'], self.Phenotype['b']]
        self.male = self.Phenotype['y']
        
        # Natural Selection Traits
        self.numBodySegments = int(max(1, self.Phenotype.get('s', 1)))
        self.speed = max(1,self.Phenotype.get('v', 5)) # Will affect hunger and water
        self.vision = max(1,self.Phenotype.get('e', 100)) / 100 # Will affect urgency 
        
        self.bodySegments = []
        for i in range(self.numBodySegments):
            newBodySegment = BodySegment(self.pos, 0.05)
            self.bodySegments.append(newBodySegment)
        self.size = self.Phenotype.get('m', 0.05) # Size will affect speed 

        # Survival Needs
        self.alert = 0.3 - self.vision/500
        self.max = 1.0 + math.log10(self.numBodySegments) * 2
        self.hunger = 1.0
        self.thirst = 1.0
        self.timer = 0

        organisms.append(self)
        speeds.append(self.speed)
        visions.append(self.vision)
        totalBodySegments.append(self.numBodySegments)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Population:", len(organisms))
        print("Average Speed:", sum(speeds)/len(speeds))
        print("Average Vision:", sum(visions)/len(visions))
        print("Average Body Segments", sum(totalBodySegments)/len(totalBodySegments))

        totalOrganisms.append(len(organisms))
        avgSpeeds.append(sum(speeds)/len(speeds))
        avgVisions.append(sum(visions)/len(visions))
        avgBodySegments.append(sum(totalBodySegments)/len(totalBodySegments))

        # y = range(organisms)
        # plt.plot(totalOrganisms, y, label = "Organisms")
        # plt.plot(avgSpeeds, y, label = "Average Speed")
        # plt.plot(avgVisions, y, label = "Average Vision")
        # plt.legend()
        # plt.show
        


    def setTarget(self):
        if abs(self.nextPos - self.pos) < self.speed * dt:
            r = self.vision * (random.random() ** 0.5)
            theta = random.random() * 2 * math.pi
            x = min(5.0,max(-5.0,self.pos.x + r * math.cos(theta)))
            y = min(5.0,max(-5.0,self.pos.y + r * math.sin(theta)))
            self.nextPos = Vec(x, y, 0)
        elif self.hunger < self.alert:
            minDist = self.vision
            food = None
            for i in foods:
                if abs(i.pos - self.pos) <= minDist:
                    minDist = abs(i.pos - self.pos)
                    food = i
            if food:
                self.nextPos = food.pos
        elif self.thirst < self.alert:
            minDist = self.vision
            pond = None
            for i in ponds:
                if abs(i.pos - self.pos) - i.r <= minDist:
                    minDist = abs(i.pos - self.pos)
                    pond = i
            if pond:
                self.nextPos = pond.pos
        elif self.timer >= 32.0 / (self.speed * 2):
            minDist = self.vision
            mate = None
            for i in organisms:
                if self == i:
                    continue
                elif abs(i.pos - self.pos) <= minDist and self.male != i.male and i.timer >= 32.0 / (i.speed * 2):
                    minDist = abs(i.pos - self.pos)
                    mate = i
            if mate:
                self.nextPos = mate.pos

    def interact(self):
        minDist = self.size
        food = None
        for i in foods:
            if abs(i.pos - self.pos) - i.r <= minDist:
                minDist = abs(i.pos - self.pos)
                food = i
        if food:
            self.hunger = min(self.max,self.hunger + food.nutrition)
            foods.remove(food)
        minDist = self.size
        pond = None
        for i in ponds:
            if abs(i.pos - self.pos) - i.r <= minDist:
                minDist = abs(i.pos - self.pos)
                pond = i
        if pond:
            self.thirst = min(self.max,self.thirst + 0.001)
        minDist = self.size
        mate = None
        for i in organisms:
            if self == i:
                continue
            elif abs(i.pos - self.pos) - i.size <= minDist and self.male != i.male and self.timer >= 32.0 / (self.speed * 2) and i.timer >= 32.0 / (i.speed * 2):
                minDist = abs(i.pos - self.pos)
                mate = i
        if mate:
            child = self.reproduce(mate)
            self.timer = 0
            mate.timer = 0

    def geneExpression(self):
        geneExp = {}
        for chromosome in self.Genotype.paternalSet:
            for gene in chromosome.genes:
                if len(gene.alleles) > 2:
                    binStr = ""
                    for allele in gene.alleles:
                        if allele.isupper():
                            binStr += "1"
                        else :
                            binStr += "0"
                    geneExp[gene.alleles[0].lower()] = int(binStr,2)
                else:
                    if gene.alleles[0].isupper():
                        geneExp[gene.alleles[0].lower()] = True
                    else:
                        geneExp[gene.alleles[0].lower()] = False
        for chromosome in self.Genotype.maternalSet:
            for gene in chromosome.genes:
                if len(gene.alleles) > 2:
                    binStr = ""
                    for allele in gene.alleles:
                        if allele.isupper():
                            binStr += "1"
                        else :
                            binStr += "0"
                    geneExp[gene.alleles[0].lower()] = (geneExp[gene.alleles[0].lower()] + int(binStr,2)) / 2
                else:
                    if gene.alleles[0].isupper():
                        geneExp[gene.alleles[0].lower()] = True
        return geneExp
    
    def reproduce(self, other):
        if (self.male and not other.male):
            return Organism(Genotype(self.Genotype.meiosis(), other.Genotype.meiosis()), (self.pos + other.pos)/2)
        elif (other.male and not self.male):
            return Organism(Genotype(other.Genotype.meiosis(), self.Genotype.meiosis()), (self.pos + other.pos)/2)
    
class BodySegment:
    def __init__(self, position, radius):
        self.pos = position
        self.r = radius

# Gene Declaration
redGene1 = Gene(['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'])
redGene2 = Gene(['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'])
greenGene1 = Gene(['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'])
greenGene2 = Gene(['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'])
blueGene1 = Gene(['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
blueGene2 = Gene(['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'])
speedGene1 = Gene(['V', 'V', 'V', 'V', 'V'])
speedGene2 = Gene(['v', 'v', 'v', 'v', 'v'])
sightGene1 = Gene(['E','E','E','E','E','E','E'])
sightGene2 = Gene(['e','e','e','e','e','e','e'])
segmentGene1 = Gene(['S', 'S', 'S'])
segmentGene2 = Gene(['s', 's', 's'])
sexGene1 = Gene(['y'])
sexGene2 = Gene(['Y'])

# Chromosome Declaration
colorCh1 = Chromosome([redGene1, greenGene1, blueGene1])
colorCh2 = Chromosome([redGene2, greenGene2, blueGene2])
speedCh1 = Chromosome([speedGene1])
speedCh2 = Chromosome([speedGene2])
sightCh1 = Chromosome([sightGene1])
sightCh2 = Chromosome([sightGene2])
segmentCh1 = Chromosome([segmentGene1])
segmentCh2 = Chromosome([segmentGene2])
sexCh1 = Chromosome([sexGene1])
sexCh2 = Chromosome([sexGene2])

genotype1 = Genotype([colorCh1, speedCh1, sightCh1, segmentCh1, sexCh1], [colorCh2, speedCh2, sightCh2, segmentCh2, sexCh2])
org1 = Organism(genotype1, Vec(0.5,0,0))

genotype2 = Genotype([colorCh1, speedCh1, sightCh1, segmentCh1, sexCh1], [colorCh2, speedCh2, sightCh2, segmentCh2, sexCh1])
org2 = Organism(genotype2, Vec(-0.5,0,0))

for i in range(10):
    newOrg = org1.reproduce(org2)