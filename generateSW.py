import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np 

#Small world network 

#Generate 500 nodes, with 10 neighbors per node，and the probability of randomized reconnection is 0.5
ws = nx.watts_strogatz_graph(500, 10, 0.5)  

#Drawing 
ps = nx.shell_layout(ws) 
plt.subplot(132) plt.title('WS') 
nx.draw(ws, ps, with_labels=True, node_color='b') 
plt.show()  

#Add np.inf to ensure complete output content 
np.set_printoptions(threshold=np.inf) 

#Convert to adjacency matrix 
a = nx.to_numpy_matrix(ws) print(a)  

#Output to a txt  
#data/task.txt：File path/TXT text name  
#self.task：The name of the array to be saved 
#fmt="%d"：To specify the saved file format, here is decimal 
#delimiter="	" The separator, separated here in the form of tab 
np.savetxt('ws500.txt', a, fmt="%d", delimiter="   ")
