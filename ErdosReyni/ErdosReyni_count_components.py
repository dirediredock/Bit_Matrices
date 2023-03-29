# by Matias I. Bofarull Oddo - 2022.01.28

import time

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

start_time = time.time()
plt.rcParams.update({"font.sans-serif": "Consolas"})
plt.rcParams.update({"font.size": 10})


def monte_carlo_simulation(n, p, simulation_num, samplings, mutable=[0]):
    monte_carlo_sample = np.zeros(simulation_num, int)
    for i in range(simulation_num):
        G = nx.erdos_renyi_graph(n, p)
        monte_carlo_sample[i] = nx.number_connected_components(G)
    list_num_components, counts = np.unique(
        monte_carlo_sample,
        return_counts=True,
    )
    mutable[0] += 1
    print(
        f"Sampling {mutable[0]} of {samplings} has taken {round(time.time() - start_time, 2)} seconds"
    )
    return list_num_components, counts


n = 100

samplings = 30
MC_simulations = 999

bound_log = np.log(n) / n
bound_mid = 1 / (n - 1)
bound_exp = 1 / (n ** (np.exp(1) - 1))

print()
print(bound_log)
print(bound_mid)
print(bound_exp)
print()

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)

for p in np.linspace(bound_log, bound_exp, num=samplings):
    X, Y = monte_carlo_simulation(n, p, MC_simulations, samplings)
    ax.plot(X, Y, linewidth=0.5, color="k")

X, Y = monte_carlo_simulation(n, bound_mid, MC_simulations, samplings)
ax.fill_between(X, Y, edgecolor="none", facecolor="k", alpha=0.2)

plt.title(
    f"nx.erdos_renyi_graph({n},p)\n\np = np.linspace(np.log(n)/n,1/n**(np.exp(1)-1),num={samplings})\n"
)
plt.xlabel(f"Number of graph components", fontweight="bold")
plt.ylabel(
    f"Occurrance across {MC_simulations} Monte Carlo simulations\n", fontweight="bold"
)

# ax.set_xscale("log")
ax.set_xticks([1, n])
plt.show()

print()

# Some references:

# https://elearning.di.unipi.it/pluginfile.php/44085/course/section/3852/Class%203_%20Random%20Networks.pdf

# https://sandipanweb.wordpress.com/2017/01/12/estimating-the-value-of-the-percolation-threshold-via-monte-carlo-simulation-in-r/
