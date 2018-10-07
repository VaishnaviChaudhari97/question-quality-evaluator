import networkx as nx
import ontologygraph
import matplotlib.pyplot as plt


def hierarchy_pos(G, root, levels=None, width=1., height=1.):
    TOTAL = "total"
    CURRENT = "current"

    def make_levels(levels, node=root, currentLevel=0, parent=None):
        if not currentLevel in levels:
            levels[currentLevel] = {TOTAL : 0, CURRENT : 0}
        levels[currentLevel][TOTAL] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            levels = make_levels(levels, neighbor, currentLevel + 1, node)
        return levels

    def make_pos(pos, node=root, currentLevel=0, parent=None, vert_loc=0):
        dx = 1/levels[currentLevel][TOTAL]
        left = dx/2
        pos[node] = ((vert_loc, left + dx*levels[currentLevel][CURRENT])*int(height))
        levels[currentLevel][CURRENT] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            pos = make_pos(pos, neighbor, currentLevel + 1, node, vert_loc+vert_gap)
        return pos
    if levels is None:
        levels = make_levels({})
    else:
        levels = {l:{TOTAL: levels[l], CURRENT:0} for l in levels}
    vert_gap = width / (max([l for l in levels])+1)
    return make_pos({})


root = input("Enter root node: ")
pos1 = hierarchy_pos(ontologygraph.g, root)
nx.draw(ontologygraph.g, pos=pos1, with_labels="True", node_color=ontologygraph.color_map, node_size=200, edge_color='grey', font_size=10)
plt.show()
