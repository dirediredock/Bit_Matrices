# by Matias I. Bofarull Oddo - 2022.12.09

import networkx as nx
import numpy as np
from algorithm_BMatrix import B_Matrix


def flip_the_bit(G):
    max_path = 1
    adjencent_nodes = G.adj
    per_node_BSF = []
    for starting_node in G.nodes():
        nodes_visited = {starting_node: 0}
        search_queue = [starting_node]
        count = 1
        while search_queue:
            next_depth = []
            extend = next_depth.extend
            for n in search_queue:
                l = [i for i in adjencent_nodes[n] if i not in nodes_visited]
                extend(l)
                for j in l:
                    nodes_visited[j] = count
            search_queue = next_depth
            count += 1
        node_distances = nodes_visited.values()
        max_node_distances = max(node_distances)
        curr_max_path = max_node_distances
        if curr_max_path > max_path:
            max_path = curr_max_path
        dict_distribution = dict.fromkeys(node_distances, 0)
        for count in node_distances:
            dict_distribution[count] += 1
        per_node_BSF.append(dict_distribution)
    return per_node_BSF


G = nx.graph_atlas(1115)

bit_flips = flip_the_bit(G)

element_wise = []
for dict in bit_flips:
    element_wise_zeros = np.zeros(
        (max([len(dict) for dict in bit_flips]), len(bit_flips)),
    )
    for i, j in dict.items():
        element_wise_zeros[i][j] = 1
    element_wise.append(element_wise_zeros)

print()
for node, bit_matrix in enumerate(element_wise):
    print(bit_matrix, node)

print()
print(G.edges)

element_sum = np.sum(element_wise, axis=0)
trim = np.where(element_sum != 0)
element_sum = element_sum[
    0 : max(trim[0]) + 1,
    0 : max(trim[1]) + 1,
]
print()
print(element_sum)

print()
print(B_Matrix(G))

print()
