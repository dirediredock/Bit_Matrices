# by Matias I. Bofarull Oddo - 2023.03.27

import networkx as nx
import numpy as np

from algorithm_Bit_Matrices import Bit_Matrices
from algorithm_BMatrix import B_Matrix


def BitMatrices_CellMap(networkx_graph):
    bit_flip_dicts = Bit_Matrices(networkx_graph)
    zeros_height = max([len(dict) for dict in bit_flip_dicts] + [2])
    zeros_width = len(bit_flip_dicts)
    BMatrix = np.zeros((zeros_height, zeros_width))
    cell_map = {}
    bit_matrices = []
    for node_index, dict in enumerate(bit_flip_dicts):
        for row in range(len(dict), zeros_height):
            dict[row] = 0
        bit_matrix = np.zeros((zeros_height, zeros_width))
        for i, j in dict.items():
            BMatrix[i][j] += 1
            bit_matrix[i][j] = 1
            if (i, j) not in cell_map:
                cell_map[(i, j)] = [node_index]
            else:
                cell_map[(i, j)].append(node_index)
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
            cell_map,
            np.array(BMatrix),
            B_Matrix(networkx_graph),
        )
    else:
        return None, None, None, None, None


# G = nx.graph_atlas(1115)
# G = nx.balanced_tree(r=2, h=4)
G = nx.read_gml("College_Football.gml", label="id")

selected_nodes = [  # some small world nodes
    7,
    8,
    22,
    51,
    68,
    77,
    78,
    108,
    111,
]

selected_nodes = [  # zeroth column nodes
    0,
    3,
    6,
    13,
    15,
    16,
    17,
    28,
    39,
    58,
    60,
    63,
    64,
    72,
    80,
    88,
    92,
    93,
    106,
]

from plot_node_link import node_link

node_link(G, selected_nodes)

bit_matrices, edgelist, node_map, BMatrix, baseline = BitMatrices_CellMap(G)

slected_matrices = []
for node, bit_matrix in enumerate(bit_matrices):
    if node in selected_nodes:
        slected_matrices.append(bit_matrix)

summed_selection = np.sum(slected_matrices, axis=0)

from plot_BMatrix_colormap import matrix_colormap

matrix_colormap(summed_selection, row_normalized=False)
matrix_colormap(summed_selection, row_normalized=True)

from plot_BMatrix_histogram import matrix_histogram

matrix_histogram(summed_selection, row_normalized=False)
matrix_histogram(summed_selection, row_normalized=True)
