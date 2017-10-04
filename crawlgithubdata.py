#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:44:52 2017

@author: hxs1943
"""

import requests
import json
import time
import os
start_time=time.time()
no_of_requests=0
###Ensures number of requests donot exceed 5000 in one hour
def limitchecker():
    global start_time
    global no_of_requests
    elapsed_time=(time.time()-start_time)/(60)
    if no_of_requests>4999 and elapsed_time<60:
        time_remaining=(60-elapsed_time)*60
        print("I am sleeping")
        time.sleep(time_remaining)
        start_time=time.time()
        no_of_requests=0
    elif elapsed_time>59:
        start_time=time.time()
        no_of_requests=0
        
####sleeps for remaining time
def sleeper():
    global start_time
    global no_of_requests
    elapsed_time=(time.time()-start_time)/(60)
    time_remaining=(60-elapsed_time)*60
    print("I am sleeping")
    time.sleep(time_remaining)
    start_time=time.time()
    no_of_requests=0
    
 #####Checkes whether there is an extra parameters if yes remove       
def modifyurl(s):
    s1=''
    for i in s:
        if (i=='{'):
            break
        else:
            s1+=i
    return s1
#####Writes json file 
def writejson(url,p,projectname,project_path):
    
    i=1
    filename=p+'_'+projectname+ '.txt'
    with open(project_path+'/'+filename,'w') as outfile:
        while True:
            global no_of_requests
            global username
            global password
            limitchecker()
            url_a=url+'?page={0}'.format(i)
            r = requests.get(url_a,auth=(username,password))
            no_of_requests=no_of_requests+1
            link=r.headers.get('link', None)
            print(link)
            if not r.json():
                break
            else:
                if r.status_code==200:
                    url_link=r.json()
                    json.dump(url_link,outfile)
                    print('No problem!!!Writing to file')
                    i+=1
                else:
                    error=r.json()
                    print(p+'\t has an error message:\n'+error['message'])
                    if r.status_code==403:
                        print(r.status_code)
                        print("I am here")
                        sleeper()
                    else:
                        break
                    
def getprojectname(url):
    count=0
    str=[]
    for a in url:
        if count>=5:
            str+=a
        if a=='/':
            count=count+1
    str=''.join(str) 
    return str   
                
        
  
#####Main program that executes
username= input("Enter github username\n")
password=input("Enter password\n")
j=1
path='/Users/hxs1943/Documents/PhD Research/Githubproject/'
with open('project_url_collection.txt') as json_file:  
    projecturllist = json.load(json_file)
for q in projecturllist:
    limitchecker()
    while True:
        if j>len(q):
            break
        eachurl=q['{0}'.format(j)]
        j=j+1
        r = requests.get(eachurl,auth=(username, password))
        if r.status_code==200:
            projectname=getprojectname(eachurl)
            project_path=path+projectname
            os.makedirs(project_path)
            url_collection=projectname+'.txt'
            with open(project_path+'/'+url_collection,'w') as outfile:
                url_link=r.json()
                json.dump(url_link,outfile)
                print('No problem!!!Writing to file url_collection')
            with open(project_path+'/'+url_collection) as infile:
                    url_list=json.load(infile)
                    i=1
            with open('parameter_url_list.txt') as json_file:  
                urllist = json.load(json_file)
                for p in urllist:
                    while True:
                        if i>len(p):
                            break
                        url_o=url_list[p['{0}'.format(i)]]
                        url_n=modifyurl(url_o)
                        writejson(url_n,p['{0}'.format(i)],projectname,project_path)
                        i=i+1
        break
    else:
        if r.status_code==403:
            error=r.json()
            print('Main URL has an error message:\n'+error['message'])
            sleeper()
        else:
            break
            
            
            
            
                       
        
        
        
        
       
   
    

    
                
        

 