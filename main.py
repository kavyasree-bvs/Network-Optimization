import algos as algos
import generate_graphs as gen_graph
import time
import generate_graphs as gg
import random
import vertex as vtx
import graph as gp


print
option = int(raw_input('Enter 0 to do custom graph testing or \n1 to test on a random sparse graph or \n2 to test on a random dense graph : '))
print 

if(option == 1):
	print 
	no_of_vertices = int(raw_input('Enter no_of_vertices for random graph generation: '))
	print
	g = gg.g_1(no_of_vertices)

if(option == 2):
	print 
	no_of_vertices = int(raw_input('Enter no_of_vertices for random graph generation: '))
	print
	g = gg.g_2(no_of_vertices)

if(option == 1 or option ==2):
	time1 = 0
	time2 = 0
	time3 = 0
	temp = ''

	print
	print 'Random graph testing starts'
	print
	for i in range(5):
		
		s1 = random.randint(1,no_of_vertices)
		t1 = s1
		while (t1 == s1):
			t1 = random.randint(1,no_of_vertices)
		
		#print 's=', s1, 't=', t1
		start = time.time()
		algos.algo1(g,s1,t1)
		time1 = time1 +  time.time()-start
		temp = temp + str(time.time()-start) + ' '	
		'''
		print '\n1 done'
		print 'time taken = ', time.time()-start
		'''
		start = time.time()
		algos.algo2(g,s1,t1)
		time2 = time2 +  time.time()-start
		temp = temp + str(time.time()-start) + ' '
		'''
		print '\n2 done'
		print 'time taken = ', time.time()-start
		'''
		start = time.time()
		algos.algo3(g,s1,t1)
		time3 = time3 +  time.time()-start
		temp = temp + str(time.time()-start) +'\n'
		'''
		print '\n3 done'
		print 'time taken = ', time.time()-start
		print '\ntimes:'
		'''
	print 'The algorithm running times are:'
	print
	print temp 

if(option == 0):
	print
	print 'Random graph testing starts'
	print

	a_l=[]
	
	n = 5

	for i in range(n+1):
		a_l.append(vtx.Vertex(i))

	g=gp.Graph(n)
	g.add_vertices([a_l[1],a_l[2],a_l[3],a_l[4],a_l[5]])
	
	g.add_edge(a_l[1],a_l[2], 1, 2)
	g.add_edge(a_l[2],a_l[4], 2, 4)
	g.add_edge(a_l[1],a_l[3], 1, 3)
	g.add_edge(a_l[3],a_l[4], 3, 4)
	g.add_edge(a_l[4],a_l[5], 4, 5)

	g.man_adj_mat[0][1] = 35
	g.man_adj_mat[1][3] = 20
	g.man_adj_mat[0][2] = 35
	g.man_adj_mat[2][3] = 25
	g.man_adj_mat[3][4] = 10
	
	g.man_adj_mat[1][0] = 35
	g.man_adj_mat[3][1] = 20
	g.man_adj_mat[2][0] = 35
	g.man_adj_mat[3][2] = 25
	g.man_adj_mat[4][3] = 10

	 
	print 'The graph is:'
	print
	print 'graph edge_weights: '
	print g.man_adj_mat
	print
	print 'graph adjacenncy list'
	print g.adjacencyList()
	print
	print 'no_of_vertices = ', n
	print

	s = int(raw_input('Enter s: '))
	print 
	t = int(raw_input('Enter t: '))

	custom_graph = [g.adjacencyList(),g.man_adj_mat]

	algos.algo1(custom_graph,s,t)
	algos.algo2(custom_graph,s,t)
	algos.algo3(custom_graph,s,t)