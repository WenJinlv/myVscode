import networkx as nx 
import matplotlib.pyplot as plt  

""" G = nx.Graph()
G.add_node(4)
G.add_node(9)
G.add_edge(4,9)
G.add_edge(3,10)
G.add_edge(3,7)
G.add_edges_from([(2,4), (1,6)])

 #create Graph by file
G = nx.read_edgelist("G:/vscode/GithubCode/myVscode/graph.txt", create_using=nx.Graph(), nodetype=int)
print(nx.info(G))
nx.draw(G)
 """
g = nx.read_edgelist("G:/vscode/GithubCode/myVscode/facebook_combined.txt", create_using=nx.Graph(), nodetype=int)
sp = nx.spring_layout(g)
plt.axis("off")
nx.draw_networkx(g, pos=sp, with_labels=False, node_size=35)
plt.show()