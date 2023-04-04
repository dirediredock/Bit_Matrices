# by Matias I. Bofarull Oddo - 2023.04.01

import networkx as nx
import numpy as np

from algorithm_Bit_Flips import Bit_Flips
from algorithm_BMatrix import B_Matrix


def Bit_Matrices(networkx_graph):
    bit_flips = Bit_Flips(networkx_graph)
    zeros_height = max([len(dict) for dict in bit_flips] + [2])
    zeros_width = len(bit_flips)
    BMatrix = np.zeros((zeros_height, zeros_width))
    cell_map = {}
    bit_matrices = []
    for node_index, dict in enumerate(bit_flips):
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
            bit_flips,
            np.array(bit_matrices),
            np.array(networkx_graph.edges),
            cell_map,
            np.array(BMatrix),
            B_Matrix(networkx_graph),
        )
    else:
        return (
            None,
            None,
            None,
            None,
            None,
        )


def node_echelons(bit_matrices):
    matrix_height = len(bit_matrices[0])
    matrix_width = len(bit_matrices[0][0])
    reachness = []
    keystoness = []
    best_hop = []
    missed_reachness = []
    missed_keystoness = []
    weightness = []
    coverage = []
    missed_coverage = []
    globality = []
    for bit_matrix in bit_matrices:
        hops = -1
        degree = []
        for row in bit_matrix:
            if row[0] == 0:
                hops += 1
            degree.append(int(np.where(row == 1)[0][0]))
        reachness.append(hops)
        keystoness.append(max(degree))
        best_hop.append(degree.index(max(degree)))
        missed_reachness.append(matrix_height - hops)
        missed_keystoness.append(matrix_width - max(degree))
        weightness.append(max(degree) / degree.index(max(degree)))
        coverage.append(max(degree) * degree.index(max(degree)))
        missed_coverage.append(
            (matrix_height * matrix_width) - (max(degree) * degree.index(max(degree)))
        )
        globality.append(
            (matrix_height * matrix_width) / (max(degree) * degree.index(max(degree)))
        )
    return (
        reachness,
        keystoness,
        best_hop,
        missed_reachness,
        missed_keystoness,
        weightness,
        coverage,
        missed_coverage,
        globality,
    )


def OBJ_to_nxflat3D(OBJ_filepath):
    with open(OBJ_filepath, "r") as f:
        lines = f.readlines()
        f.close()
    G = nx.Graph()
    flat3D_pos = {}
    node_count = 1
    for line in lines:
        if line.startswith("v "):
            coords = tuple(map(float, line.split()[1:]))
            G.add_node(node_count)
            flat3D_pos[node_count] = np.array(
                [
                    float(coords[0]),  # camel fox [2]
                    float(coords[1]),  # camel fox [1]
                ]
            )
            node_count += 1
        elif line.startswith("f "):
            face = line.split()[1:]
            face = [int(i.split("/")[0]) for i in face]
            G.add_edge(int(face[0]), int(face[1]))
            G.add_edge(int(face[1]), int(face[2]))
    return G, flat3D_pos


# G = nx.graph_atlas(1115)
# G = nx.balanced_tree(r=2, h=4)
# G = nx.read_edgelist("bunny_edgelist.csv", delimiter=",", nodetype=str)
# G = nx.grid_2d_graph(2, 25)
# G = nx.read_edgelist("data/data_CSV/infobox_network_Fortran.tsv")
# G = nx.read_gml("data/data_GML/Western_States_Power_Grid.gml", label="id")
# G = nx.read_gml("data/data_GML/College_Football.gml", label="id")
# G = nx.read_gml("data/data_GML/Doubtful_Sound_Dolphins.gml", label="id")
# G = nx.read_gml("data/data_GML/Les_Miserables.gml", label="id")
# G = nx.read_gml("data/data_GML/Zacharys_Karate_Club.gml", label="id")
# G = nx.read_edgelist(
#     # "data/data_OBJ/bunny.csv",
#     "data/data_OBJ/camel.csv",
#     # "data/data_OBJ/cube.csv",
#     # "data/data_OBJ/cyl1.csv",
#     # "data/data_OBJ/cyl2.csv",
#     # "data/data_OBJ/icos.csv",
#     # "data/data_OBJ/sphere1.csv",
#     # "data/data_OBJ/teapot.csv",
#     # "data/data_OBJ/tet.csv",
#     delimiter=",",
#     nodetype=str,
# )

# flat3D_pos = nx.spring_layout(G, seed=42)

G, flat3D_pos = OBJ_to_nxflat3D("data/data_OBJ/bunny.obj")

G.remove_edges_from(nx.selfloop_edges(G))

print("START")

(
    bit_flips,
    bit_matrices,
    edgelist,
    cell_map,
    BMatrix,
    expect,
) = Bit_Matrices(G)

print("Bit_Matrix DONE")

(
    reachness,
    keystoness,
    best_hop,
    missed_reachness,
    missed_keystoness,
    weightness,
    coverage,
    missed_coverage,
    globality,
) = node_echelons(bit_matrices)

print("Node_Echelons DONE")

from plot_node_link import node_flat3D

print("Start Plotting")

node_flat3D(G, missed_reachness, flat3D_pos, size=20)  # camel size=60, bunny 20
