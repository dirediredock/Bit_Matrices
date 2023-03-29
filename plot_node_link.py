# by Matias I. Bofarull Oddo - 2022.12.07

import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams.update({"font.sans-serif": "Consolas"})
plt.rcParams.update({"font.size": 10})


def node_link(G):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # positions = nx.get_node_attributes(G, "pos")

    options = {
        "node_color": "w",
        "node_size": 300,
        "width": 1,
        "with_labels": True,
        "font_color": "k",
        "font_weight": "bold",
        "font_size": 10,
    }
    nx.draw_networkx(G, **options)

    plt.title(
        "Nodes | " + str(G.number_of_nodes()) + "\nEdges | " + str(G.number_of_edges()),
        weight="bold",
        linespacing=1,
        loc="left",
    )

    plt.show()
