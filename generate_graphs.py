import graph as gp
import vertex as vtx
import random
import time

def g_1(no_of_vertices):
	V = []
	a_l=[]
	for i in range(no_of_vertices+1):
		a_l.append(vtx.Vertex(i))

	for i in range(no_of_vertices+1):
		V.append(i)

	g = gp.Graph(no_of_vertices)
	 
	g.add_vertices(V[1:])

	edge_count = 0
	for i in range(1,no_of_vertices):
		g.add_edge(a_l[i],a_l[i+1],i,i+1)
		#print i,i+1
		edge_count = edge_count +1
		
	g.add_edge(a_l[no_of_vertices],a_l[1],no_of_vertices,1)
	edge_count = edge_count +1

	#Sparse graph
	avg_vertex_degree = 8
	no_of_edges = (avg_vertex_degree/2) * no_of_vertices
	start = time.time()

	def non_adjacent_vertices(index):
		p =[]
		if(index != no_of_vertices and index !=1):
			p= V[index+2:]
		if(index == 1):
			p= V[index+2:-1]
		return p

	non_adj_V = []
	non_adj_V.append([])

	for i in range(no_of_vertices):
		non_adj_V.append( non_adjacent_vertices(i+1))

	comb=[]
	for i in range(1,len(non_adj_V)):
		for j in range(len(non_adj_V[i])):
			comb.append([i,non_adj_V[i][j]])
	ee =  random.sample(comb, no_of_edges-no_of_vertices)

	for i in range(len(ee)):
		g.add_edge(a_l[ee[i][0]],a_l[ee[i][1]],ee[i][0],ee[i][1])
		edge_count = edge_count +1
	adj_list = g.adjacencyList() 
	adj_mat = g.adjacency_matrix
	

	print 'Sparse graph generated. edge_count =', edge_count
	print 'It took', time.time()-start, 'seconds to generate the graph.'
	ret = [adj_list,adj_mat]
	return ret

def g_2(no_of_vertices):
	V = []
	a_l=[]


	for i in range(no_of_vertices+1):
		a_l.append(vtx.Vertex(i))

	for i in range(no_of_vertices+1):
		V.append(i)

	g = gp.Graph(no_of_vertices)
	 
	g.add_vertices(V[1:])

	edge_count = 0
	for i in range(1,no_of_vertices):
		g.add_edge(a_l[i],a_l[i+1],i,i+1)
		#print i,i+1
		edge_count = edge_count +1
		
	g.add_edge(a_l[no_of_vertices],a_l[1],no_of_vertices,1)
	edge_count = edge_count +1

	#Dense graph
	start = time.time()

	for i in range(no_of_vertices):
		for j in range(i+2, no_of_vertices):
			probab = random.randint(0,100)
			if(i==0 and j== no_of_vertices-1):
				continue
			if(probab <= 20):
				g.add_edge(a_l[i+1],a_l[j+1],i+1,j+1)
				edge_count = edge_count +1
	adj_list = g.adjacencyList() 
	adj_mat = g.adjacency_matrix

	print 'Dense graph generated. edge_count =', edge_count
	print 'It took', time.time()-start, 'seconds to generate the graph.'
	ret = [adj_list,adj_mat]
	return ret


#print g_2(10)