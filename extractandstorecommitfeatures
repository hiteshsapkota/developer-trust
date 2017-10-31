#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 22:47:37 2017

@author: hxs1943
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:25:45 2017

@author: hxs1943
"""

import json
import csv
source_path=input('Enter the path where github repositories are stored\n')
destination_path=input('Enter path inorder to store data\n')
commitrecord={}
commitrecord['commits']=[]
with open(destination_path+'/'+'commitrecord.json','w') as outfile:
    json.dump(commitrecord,outfile)

flag=False
name=False
###Reads project lists from csv file

with open(destination_path+'/'+'commitrecord.json','r+') as infile:
    commitrecord=json.load(infile)
with open('all_projects.csv', 'r') as csvfile:
    projectlist = csv.DictReader(csvfile)

    for row in projectlist:
            if row['language']=='Python':
                projectname=row['repo_name']
                print("I am currently working on repository:"+projectname)
                with open(source_path+'/'+projectname+'/'+'commits_url_'+projectname+'.json') as json_file:
                    commit = json.load(json_file)
                    i=-1
                    while True:
                        i=i+1
                        try:
                            
                                if not flag:
                                    flag=True
                                    commitrecord['commits'].append({
                                            'name':commit[i]['commit']['committer']['name'],
                                            'email':commit[i]['commit']['committer']['email'],
                                            'noofcommits':1,
                                            'repositoryname':projectname})  
                                else:
                                    for c in commitrecord['commits']:
                                        if(c['email']==commit[i]['commit']['committer']['email'] and c['repositoryname']==projectname and c['name']==commit[i]['commit']['committer']['name']):
                                            name=True;
                                            c['noofcommits']=c['noofcommits']+1
                                    if name==False:
                                        commitrecord['commits'].append({
                                                'name':commit[i]['commit']['committer']['name'],
                                                'email':commit[i]['commit']['committer']['email'],
                                                'noofcommits':1,
                                                'repositoryname':projectname}) 
                                name=False
                                 
          
            
                        except IndexError:
                            break
    infile.seek(0)
    json.dump(commitrecord,infile) 
