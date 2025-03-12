# Where stuff is made

import uuid
from vectors import*
import random
import networkx as nx
import matplotlib as plt

class Ball:

    def __init__(self,velocity):

        self.pos = Vec(0,0,0)
        self.vel = velocity
        self.acc = None
        self.r = 0.021335
        self.m = 0.045
        self.genetics = ball.create_chromosome()
        self.visible=True
    
    def create_chromosome():
        return {
            "id": str(uuid.uuid4()),
            "Vx": random.uniform(0,3),
            "Vy": random.uniform(0,3),
            "parent_ids": None
        }
    
    def arithemetic_crossover_with_lineage(parent1, parent2, alpha = 0.5, mutation_rate = 0.1):
        Vx1, Vy1 = parent1["Vx"], parent1["angle"]
        Vx2, Vy2 = parent2["Vx"], parent2["angle"]

        # I should change to allow for variable number of kids
        child1 = {
            "id": str(uuid.uuid4()),
            "Vx": alpha * Vx1 + (1 - alpha) * Vx2,
            "Vy": alpha * Vy1 + (1 - alpha) * Vy2,
            "parent_ids": (parent1["id"], parent2["id"])
        }

        child2 = {
            "id": str(uuid.uuid4()),
            "Vx": (1 - alpha) * Vx1 + alpha * Vx2,
            "Vy": (1 - alpha) * Vy1 + alpha * Vy2,
            "parent_ids": (parent1["id"], parent2["id"])
        }

        child1 = ball.mutate(child1, mutation_rate)
        child2 = ball.mutate(child2, mutation_rate)

        return child1, child2
    
    def mutate(chromosome, mutation_rate = 0.1, mutation_strength = 5):
        if random.random() < mutation_rate:
            chromosome["Vx"] += random.uniform(-mutation_strength, mutation_strength)
            chromosome["Vx"] += max(0, chromosome("Vx"))

        if random.random() < mutation_rate:
            chromosome["Vy"] += random.uniform(-mutation_strength, mutation_strength)
            chromosome["Vy"] += max(0, chromosome("Vy"))
        
        return chromosome


    # def visualize_lineage(population):
    #     G = nx.DiGraph()
    #     for individual in population:
    #         G.add_node(individual["id"], label=f'V:{individual["velocity"]:.1f}, θ:{individual["angle"]:.1f}')
        
    #         if individual["parent_ids"]:
    #             parent1, parent2 = individual["parent_ids"]
    #             G.add_edge(parent1, individual["id"])
    #             G.add_edge(parent2, individual["id"])

    #     plt.figure(figsize=(10, 6))
    #     pos = nx.spring_layout(G, seed=42, k=0.8)  # Layout for better spacing
    #     labels = nx.get_node_attributes(G, 'label')
    
    #     nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=1000, font_size=8)
    #     nx.draw_networkx_labels(G, pos, labels, font_size=6)
    
    #     plt.title("Genetic Algorithm Lineage Tree")
    #     plt.show()



populationSize, families = 200, 10
population = []
winners = []
losers = []
finished = 0
final = []

ball=Ball(Vec(0.05,2.45,0))