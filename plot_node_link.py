# by Matias I. Bofarull Oddo - 2022.12.07

import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams.update({"font.sans-serif": "Consolas"})
plt.rcParams.update({"font.size": 10})


def node_link(G, selected_nodes):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # positions = nx.get_node_attributes(G, "pos")

    color_map = []
    for node in G:
        if node in selected_nodes:
            color_map.append("tab:red")
        else:
            color_map.append("w")

    options = {
        # "node_color": "w",
        "node_size": 200,
        "width": 0.75,
        "with_labels": True,
        "font_color": "k",
        "font_weight": "bold",
        "font_size": 7,
    }
    nx.draw_networkx(G, node_color=color_map, **options)
    plt.title(
        "Nodes | " + str(G.number_of_nodes()) + "\nEdges | " + str(G.number_of_edges()),
        weight="bold",
        linespacing=1,
        loc="left",
    )

    plt.show()
