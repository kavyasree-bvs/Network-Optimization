CSCE 629: COURSE PROJECT -- README.TXT
BY -- Venkata Satya Kavya Sree Bondapalli

This file describes the content of this directory. And the instructions to follow for executing the code.


COMPILATION:
===========
pre-requisite		Python 2.7.6 installed on the system
Command			python main.py

CONTENTS:
===========
FILE: 			DESCRIPTION:

graph.py		Contains the class for a graph.
vertex.py		Contains the class for a vertex.
heap.py			Contains the heap data structure with DEL,MAX,INSERT sub-routines and HeapSort function.
generate_graphs.py	Contains the functions for generating a random sparse(G1) or a random dense(G2) graph.
algos.py		Contains the implementations of the following functions:
			algo1(g,s,t) Dijkstra's without heap
			algo2(g,s,t) Dijkstra's with heap
			algo3(g,s,t) Kruskal's with edges sorted using HeapSort
main.py			This is the main file through which testing is done.
sparse_results.txt	Contains the sparse graph test results printed to the console
dense_results.txt	Contains the dense graph test results printed to the console
Report.pdf		The report
