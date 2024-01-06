import networkx as nx
import json

# Input data
data = 

# Create a graph
G = nx.Graph()

# Add edges from neighborhoods to restaurants
restaurant_distances = data["restaurants"]["r0"]["neighbourhood_distance"]
for i, d in enumerate(restaurant_distances):
    G.add_edge("r0", f"n{i}", weight=d)

# Add edges between neighborhoods
neighborhoods = data["neighbourhoods"]
for n, info in neighborhoods.items():
    distances = info["distances"]
    for i, d in enumerate(distances):
        G.add_edge(n, f"n{i}", weight=d)

# Solve the TSP
tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True)

# Prepare the output
output = {
    "v0": {
        "path": tsp_path
    }
}

# Convert the output to JSON format
output_json = json.dumps(output, indent=4)
print(output_json)
