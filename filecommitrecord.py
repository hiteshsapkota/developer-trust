#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:14:10 2017

@author: hxs1943
"""
import csv
import json
import requests
login_number=0;
i=0;
def createcommitfile(projectname,destination_path):
    filecommitrecord={}
    filecommitrecord['developers']=[]
    with open(destination_path+'/'+projectname+"_"+"filecommitrecord.json",'w') as outfile:
        json.dump(filecommitrecord,outfile)
        
def loadcommitrecord(projectname,source_path):
    with open(source_path+'/'+projectname+'/'+'commits_url_'+projectname+'.json') as json_file:
        commits = json.load(json_file)
        return commits
def openauthenticationfile(authentication_path):
    with open(authentication_path+"/authentication.json") as outfile:
        authentication=json.load(outfile)
        return authentication
    
def loadfilerecord(projectname,commit,authentication):
    global login_number
    
    r = requests.get(commit['url'],auth=(authentication[login_number]['username'],authentication[login_number]['password']))
    if r.status_code==200:
        print("I am working well")
        filelink=r.json()
    else:
        error=r.json()
        print(projectname+'\t has an error message:\n'+error['message'])
        if r.status_code==403:
            print(r.status_code)
            while True:
                if login_number<18:
                    login_number=login_number+1
                else:
                     login_number=0
                r = requests.get(commit['url'],auth=(authentication[login_number]['username'],authentication[login_number]['password']))
                if r.status_code==200:
                   filelink=r.json()
                   break;
        else:
            filelink=[];
            
    return filelink
                
def initializedeveloperrecord(filecommitrecord,filelink,commit):
    
        global i
    
        filecommitrecord['developers'].append({
                                        "name":commit['commit']['committer']['name'],
                                        "email":commit['commit']['committer']['email'],
                                        "noofcommits":1,
                                        "files":{
                                                        
                                                }
                                                    
                                                    
                                        })

        for file in filelink['files']:
            filecommitrecord['developers'][0]['files'][file['filename']]=1
        i=i+1
    
   
                   
def appendfilerecord(filecommitrecord,filelink,commit):
    global i
    samedev=False
    for developer in filecommitrecord['developers']:
        
        if developer['name']==commit['commit']['committer']['name'] and developer['email']==commit['commit']['committer']['email']:
            samedev=True
            developer['noofcommits']=developer['noofcommits']+1
            for file1 in filelink['files']:
                newfile=True   
                for k,v in developer['files'].items():
                    if k==file1['filename']:
                        developer['files'][k]=developer['files'][k]+1
                        newfile=False
                if newfile==True:
                    developer['files'][file1['filename']]=1
    if samedev==False:
            
             filecommitrecord['developers'].append({
                                        "name":commit['commit']['committer']['name'],
                                        "email":commit['commit']['committer']['email'],
                                        "noofcommits":1,
                                        "files":{
                                                        
                                                }
                                                    
                                                    
                                           })
             for file in filelink['files']:
                 filecommitrecord['developers'][i]['files'][file['filename']]=1 
             i=i+1
             
            
    
source_path=input('Enter path where github repositories are stored\n')
destination_path=input('Enter path inorder to store data\n')
authentication_path=input('Enter path where authentication file is located\n')
csv_path=input('Enter the path where csv files are located \n')
authentication=openauthenticationfile(authentication_path)
with open(csv_path+'/'+'all_projects.csv', 'r') as csvfile:
        projectlist = csv.DictReader(csvfile)
        for row in projectlist:
            if row['language']=='Python':
                projectname=row['repo_name']
                print("I am currently working on repository:"+projectname)
                initialflag=True
                i=0;
                createcommitfile(projectname,destination_path)
                ##Opens existing file####
                with open(destination_path+'/'+projectname+"_"+"filecommitrecord.json",'r+') as infile:
                     filecommitrecord=json.load(infile)
                     commits=loadcommitrecord(projectname,source_path)
                     for commit in commits:
                         filelink=loadfilerecord(projectname,commit,authentication)
                         if len(filelink)!=0:
                             if initialflag is True:
                                 initialflag=False
                                 initializedeveloperrecord(filecommitrecord,filelink,commit)
                             else:
                                 appendfilerecord(filecommitrecord,filelink,commit)
                     infile.seek(0)
                     json.dump(filecommitrecord,infile) 
                                 
                         
                
       