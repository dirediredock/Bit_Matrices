# Bit_Matrices

2022.03.29 - The newest version of the Bmatrix algorithms output the following data structures:

  - `edgelist`        Input, the edgelist fed into the algorithm (read by the networkx library).
  
  - `bit_matrices`    New output, this is a list of matrices made of 1s and 0s, one for each node in
                  the network and placed within the list by node index.
                  
  - `cell_map`        New output, a dictionary with tuple keys (i,j) for all non-zero BMatrix cells,
                  each key/cell has the list of node indices contributing to that cell. This step
                  adds the zeroth column bit-flips to the bit_flips dictionary, fixing the need
                  of calculating the zeroth column values manually. This is possible by knowing
                  the BMatrix height from the outset, and also knowing that a Bmatrix will always
                  have at minium two rows.
                  
  - `BMatrix`         New output, a final Bmatrix calculated from the element-wise adition of the
                  bit_matrices list.
                  
  - `bit_flips`       Old output, the dictionaries from the BFS traversal from the original Bagrow
                  algorithm.
                  
  - `expect`          Old output, an independent call to the original complete BMatrix algorithm to
                  have a BMatrix to compare (test) against.
                                  
For a benchmarking and sanity check that this new path to calculating BMatrix results in the same BMatrix as the original algorithm, I tested all the networks in the graph_atlas corpus. All tests passed expect for the graphs with edgless nodes (2, 3, 4, 5, 6, and 7 nodes as point clouds). In this cases the new BMatrix gave an output of only the zeroth row, where what is missing is the first row (histogram of node degrees) where the zeroth cell has a value of all node counts and the first cell has a value of zero. This is fixed by enforcing a minimum height of 2 from the outset. There may be an interesting mathmetical discussion here on whether a histogram for point clouds is even meaningful. Also, is there a "ghost" last row in every BMatrix?
                  
                  
