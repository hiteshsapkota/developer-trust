#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:24:41 2017

@author: hxs1943
"""

###This program loads  developer relationship json file(based on file sharing), interprets file, constructs dsn and store network into dsn pickle file
import json
import networkx as nx
source_path=input('Enter the path where developerrelationfile located \n')
destination_path=input('Enter the path where you want to store social network \n')
no_of_dev=[]
i_value=[]
G=nx.Graph()
with open(source_path+"/"+"filedevrelation.json") as outfile:
    filedevrelation=json.load(outfile)
    for developer in filedevrelation['developers']:
            if developer['name']!="GitHub":
                for name,fileno in developer['friends'].items():
                    if name!="GitHub" and developer['name']!=name:
                        G.add_edge(developer['name'],name,weight=fileno)
         
H=nx.Graph()
if nx.number_connected_components(G)>1:
    for g in nx.connected_component_subgraphs(G):
        if nx.number_of_nodes(g)>100:
            H=G.subgraph(g)
                       
nx.write_gpickle(H,destination_path+"/"+"filebaseddsn.gpickle")