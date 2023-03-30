# by Matias I. Bofarull Oddo - 2023.03.27


def Bit_Matrices(G):
    max_path = 1
    adjencent_nodes = G.adj
    per_node_traverse = []
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
        per_node_traverse.append(dict_distribution)
    return per_node_traverse
