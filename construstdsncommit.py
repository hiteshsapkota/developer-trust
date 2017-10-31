
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:43:41 2017

@author: hxs1943
"""
##This program reads commit related json file and constructs developer social network based on commit
import json
import networkx as nx
G=nx.Graph()
####Load json file
source_path=input("Enter the path where json file related to commit is present\n")
with open(source_path+'/'+'githubcommitrecord.json') as infile:
    commitrecord = json.load(infile)
i=0; 
a=False; 
b=0;
while True:
    try:
        
        for j in range(0,i-1):
            if commitrecord['commits'][j]['name']==commitrecord['commits'][i]['name'] and commitrecord['commits'][j]['email']==commitrecord['commits'][i]['email']:
               a=True; 
            if commitrecord['commits'][j]['repositoryname']==commitrecord['commits'][i]['repositoryname']:
                G.add_edge(commitrecord['commits'][j]['name'],commitrecord['commits'][i]['repositoryname'],weight=min(commitrecord['commits'][j]['noofcommits'],commitrecord['commits'][i]['noofcommits']))
        if not a==True:
            
            b=b+1;
            print(b)
            G.add_node(commitrecord['commits'][i]['name'],email=commitrecord['commits'][i]['email'],repositoryname=commitrecord['commits'][i]['repositoryname']) 
            
        a=False;   
        i=i+1
    except IndexError:
        break
nx.draw(G)
