import csv
import random
import networkx as nx
import matplotlib.pyplot as plt
with open('sample.csv') as filevar:
    filevar = csv.reader(filevar)
    headers = next(filevar)
    rows = [row for row in filevar]
    factors = list(set([row[0] for row in rows]))
    ids= list(set([row[1] for row in rows]))
    weights= list(set([row[2] for row in rows]))
    B=nx.DiGraph()
X=factors
Y=ids
Z=weights
B.add_nodes_from(X)
B.add_nodes_from(Y)
B.add_weighted_edges_from(rows)
pos = nx.spring_layout(B, k=0.50)
scc = list(nx.strongly_connected_components(B)) 
print scc
print nx.number_strongly_connected_components(B)
iterations=10000
p=0.1
seed_set=random.sample(B.node(), 5)
avg_influence=0.0
for i in range(iterations):
    S=list(seed_set)
    for i in range(len(S)):
        for neighbor in B.neighbors(S[i]):
            if random.random()<p:
                if neighbor not in S:
                    S.append(neighbor)
    avg_influence+=(float(len(S))/iterations)
print 'Total influence:',int(round(avg_influence))
nx.draw(B, pos=pos, k=0.5, with_labels=True)
plt.savefig("graph5.png")
plt.show()
