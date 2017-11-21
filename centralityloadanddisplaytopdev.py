#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:18:07 2017

@author: hxs1943
"""

###This program lists top n developers with this attributes based on type of centrality you want to measure
import networkx as nx
import operator
cent_path=input("Enter the path where centrality file is located \n")
cent_type=input("Enter the type of centrality you want to determine d for degree,b for betweenness,c for closeness and p for pagerank \n" )
no_of_dev=int(input("Input number of top developers you want to list \n"))
if cent_type=="d":
    deg_cent=nx.read_gpickle(cent_path+"/"+"degreecentrality.gpickle")
    print(sorted(deg_cent.items(),key=operator.itemgetter(1),reverse=True)[0:no_of_dev])

if cent_type=="b":
    deg_cent=nx.read_gpickle(cent_path+"/"+"betweennesscentrality.gpickle")
    print(sorted(deg_cent.items(),key=operator.itemgetter(1),reverse=True)[0:no_of_dev])
    
if cent_type=="c":
    deg_cent=nx.read_gpickle(cent_path+"/"+"closenesscentrality.gpickle")
    print(sorted(deg_cent.items(),key=operator.itemgetter(1),reverse=True)[0:no_of_dev])
if cent_type=="p":
    deg_cent=nx.read_gpickle(cent_path+"/"+"pagerankcentrality.gpickle")
    print(sorted(deg_cent.items(),key=operator.itemgetter(1),reverse=True)[0:no_of_dev])