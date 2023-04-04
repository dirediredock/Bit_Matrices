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
        # "node_color": "w",
        "node_size": 200,
        "width": 0.75,
        "with_labels": True,
        "font_color": "k",
        "font_weight": "bold",
        "font_size": 7,
    }
    nx.draw_networkx(G, **options)
    plt.title(
        "Nodes | " + str(G.number_of_nodes()) + "\nEdges | " + str(G.number_of_edges()),
        weight="bold",
        linespacing=1,
        loc="left",
    )

    plt.show()


def node_attribute(G, color_nodes, labels=False, size=100):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # positions = nx.get_node_attributes(G, "pos")

    # color_map = []
    # for node in G:
    #     if node in selected_nodes:
    #         color_map.append("tab:red")
    #     else:
    #         color_map.append("w")

    vmin = min(color_nodes)
    vmax = max(color_nodes)
    cmap = plt.cm.inferno

    options = {
        # "node_color": "w",
        "node_size": size,
        "width": 0.75,
        "with_labels": labels,
        "font_color": "k",
        "font_weight": "bold",
        "font_size": 7,
        "cmap": cmap,
        "vmin": vmin,
        "vmax": vmax,
    }
    nx.draw_networkx(G, node_color=color_nodes, **options)

    sm = plt.cm.ScalarMappable(
        cmap=cmap,
        norm=plt.Normalize(vmin=vmin, vmax=vmax),
    )
    sm.set_array([])
    plt.colorbar(sm, aspect=42)

    plt.title(
        "Nodes | " + str(G.number_of_nodes()) + "\nEdges | " + str(G.number_of_edges()),
        weight="bold",
        linespacing=1,
        loc="left",
    )

    plt.show()


def node_flat3D(G, color_nodes, flat3D_pos, size=50):
    fig = plt.figure(figsize=(9, 9))

    ax_hist = fig.add_axes([0.808, 0.11, 0.08, 0.77])
    ax_hist.hist(
        color_nodes,
        bins=100,
        orientation="horizontal",
        color="whitesmoke",
    )
    ax_hist.margins(y=0)
    ax_hist.axis("off")

    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    vmin = min(color_nodes)
    vmax = max(color_nodes)
    cmap = plt.cm.inferno

    options = {
        # "node_color": "w",
        "node_size": size,
        "width": 0.75,
        "with_labels": False,
        "font_color": "k",
        "font_weight": "bold",
        "font_size": 7,
        "cmap": cmap,
        "vmin": vmin,
        "vmax": vmax,
    }
    nx.draw_networkx(G, node_color=color_nodes, pos=flat3D_pos, **options)

    sm = plt.cm.ScalarMappable(
        cmap=cmap,
        norm=plt.Normalize(vmin=vmin, vmax=vmax),
    )
    sm.set_array([])
    plt.colorbar(sm, aspect=42)

    plt.title(
        "Nodes | " + str(G.number_of_nodes()) + "\nEdges | " + str(G.number_of_edges()),
        weight="bold",
        linespacing=1,
        loc="left",
    )

    plt.show()
