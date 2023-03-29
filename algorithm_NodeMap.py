# by Matias I. Bofarull Oddo - 2023.03.27

import networkx as nx
import numpy as np

from algorithm_Bit_Matrices import Bit_Matrices
from algorithm_BMatrix import B_Matrix
from plot_node_link import node_link


def BitMatrices_NodeMap(networkx_graph):
    bit_flip_dicts = Bit_Matrices(networkx_graph)
    zeros_height = max([len(dict) for dict in bit_flip_dicts])
    zeros_width = len(bit_flip_dicts)
    BMatrix = np.zeros((zeros_height, zeros_width))
    node_map = {}
    bit_matrices = []
    for node_index, dict in enumerate(bit_flip_dicts):
        for row in range(len(dict), zeros_height):
            dict[row] = 0
        bit_matrix = np.zeros((zeros_height, zeros_width))
        for i, j in dict.items():
            BMatrix[i][j] += 1
            bit_matrix[i][j] = 1
            if (i, j) not in node_map:
                node_map[(i, j)] = [node_index]
            else:
                node_map[(i, j)].append(node_index)
        bit_matrices.append(bit_matrix)
    trim = np.where(BMatrix != 0)
    BMatrix = BMatrix[
        0 : max(trim[0]) + 1,
        0 : max(trim[1]) + 1,
    ]
    for i in range(len(bit_matrices)):
        bit_matrices[i] = bit_matrices[i][
            0 : max(trim[0]) + 1,
            0 : max(trim[1]) + 1,
        ]
    if (np.array(BMatrix) == B_Matrix(networkx_graph)).all():
        return (
            np.array(bit_matrices),
            np.array(networkx_graph.edges),
            node_map,
            np.array(BMatrix),
            B_Matrix(networkx_graph),
        )
    else:
        return None, None, None, None, None


# G = nx.graph_atlas(1115)
G = nx.balanced_tree(r=2, h=4)

# for i in range(2, 300):  # 1253
#     print(i, end=" ")
#     G = nx.graph_atlas(i)
#     BitMatrices_NodeMap(G)

node_link(G)

bit_matrices, edgelist, node_map, BMatrix, baseline = BitMatrices_NodeMap(G)

print()
for node, bit_matrix in enumerate(bit_matrices):
    print(bit_matrix, node)
    print()
print(edgelist)
print()
for matrix_ij, node_contribution in node_map.items():
    print(matrix_ij, node_contribution)
print()
print(BMatrix)
print()
print(baseline)
print()
