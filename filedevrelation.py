#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:06:38 2017

@author: hxs1943
"""

import json
import csv
j=0;
k=0;
initialflag=True
def createcommitfile(dest_path):
    filedevrelation={}
    filedevrelation['developers']=[]
    with open(dest_path+"/"+"filedevrelation.json",'w') as outfile:
        json.dump(filedevrelation,outfile)
        
def loadcommitrecord(projectname,source_path):
    with open(source_path+'/'+projectname+'_filecommitrecord.json') as json_file:
        filecommitrecord = json.load(json_file)
        return filecommitrecord
def openauthenticationfile(authentication_path):
    with open(authentication_path+"/authentication.json") as outfile:
        authentication=json.load(outfile)
        return authentication
    
def initializedevrecord(developer,filedevrelation,projectname,k):
    
    
        filedevrelation['developers'].append({
                                        "name":developer['name'],
                                        "email":developer['email'],
                                        "friends":
                                            {
                                             
                                                    }
                                                 
                                        })
       
        
       
   
                   
def appendfilerecord(projectname,filedevrelation,filecommitrecord,developer,toaldeveloper,j,k):
    for i in range(j+1,totaldeveloper):
        devexist=False
        for file_others in filecommitrecord['developers'][i]['files']:
            samefile=False
            for file_own in developer['files']:
                if file_own==file_others:
                    samefile=True
            if samefile is True:
                if devexist is False:
                    devexist=True
                    filedevrelation['developers'][k]['friends'][filecommitrecord['developers'][i]['name']]=1
                else:
                    filedevrelation['developers'][k]['friends'][filecommitrecord['developers'][i]['name']]+=1
                    
                
        
            
    
def findtotaldeveloper(filecommitrecord):
    total_developer=0
    for developer in filecommitrecord['developers']:
       total_developer=total_developer+1
    return total_developer
def loadcsvprojects(csv_path):
    with open(csv_path+'/'+'all_projects.csv', 'r') as csvfile:
        projectlist = csv.DictReader(csvfile)
        return projectlist
    
    
def addfilerecordexisting(filecommitrecord,developern,developero):
    for i in range(j+1,totaldeveloper):
        devexist=False
        for file_others in filecommitrecord['developers'][i]['files']:
            samefile=False
            for file_own in developero['files']:
                if file_own==file_others:
                    samefile=True
            if samefile is True:
                if devexist is False:
                    devexist=True
                    developern['friends'][filecommitrecord['developers'][i]['name']]=1
                else:
                    developern['friends'][filecommitrecord['developers'][i]['name']]+=1
    




    
csv_path=input('Enter the path where csv files are located \n')
source_path=input('Enter the path where filecommitrecord files are stored \n')
dest_path=input('Enter the path where you want to store developer relation file \n')
createcommitfile(dest_path)
#projectlist=loadcsvprojects(csv_path)
with open(dest_path+'/'+"filedevrelation.json",'r+') as infile:
    filedevrelation=json.load(infile)
    with open(csv_path+'/'+'all_projects.csv', 'r') as csvfile:
        projectlist = csv.DictReader(csvfile)
        for row in projectlist:
            if row['language']=='Python':
                projectname=row['repo_name']
                filecommitrecord=loadcommitrecord(projectname,source_path)
                totaldeveloper=findtotaldeveloper(filecommitrecord)
                j=0;
                for developero in filecommitrecord['developers']:
                    samedev=False
                    for developern in filedevrelation['developers']:
                        if developero['name']==developern['name'] and developero['email']==developern['email']:
                            samedev=True
                            addfilerecordexisting(filecommitrecord,developern,developero)
                    if samedev is False:
                        initializedevrecord(developero,filedevrelation,projectname,k)
                        appendfilerecord(projectname,filedevrelation,filecommitrecord,developero,totaldeveloper,j,k)
                        k=k+1
                    j=j+1
            
                        
    infile.seek(0)
    json.dump(filedevrelation,infile) 
                                 
                         