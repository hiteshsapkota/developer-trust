#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:35:58 2017

@author: hxs1943
"""
import networkx as nx
###This program loads network, calculates degree, closeness, betweennes and pagerank centrality and stores data 
source_path=input('Enter the path where social network is located \n')
destination_path=input('Enter the path where you want to store different centrality files \n')
G=nx.read_gpickle(source_path+"/"+"filebaseddsn.gpickle")
###Calculate and store degree centrality for each node
degCent=nx.degree_centrality(G)
nx.write_gpickle(degCent,destination_path+"/"+"degreecentrality.gpickle")
###Calculate and store closeness centrality for each node
closeCent=nx.closeness_centrality(G,normalized=True)
nx.write_gpickle(closeCent,destination_path+"/"+"closenesscentrality.gpickle")
###Calculate and store betweenness centrality for each node
btwnCent=nx.betweenness_centrality(G,normalized=True,endpoints=False,k=1000)
nx.write_gpickle(btwnCent,destination_path+"/"+"betweennesscentrality.gpickle")
###Calculate and store pagerank centrality for each node
page_rank=nx.pagerank(G,alpha=0.8)
nx.write_gpickle(page_rank,destination_path+"/"+"pagerankcentrality.gpickle")