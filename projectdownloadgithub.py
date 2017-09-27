#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:25:54 2017

@author: hxs1943
"""
import requests

#url = 'https://api.github.com/repos/hiteshsapkota/firstproject/commits'

####Empty follower json file#####
#####Empty Following json file####
####Requires authentication to get collaborators#####
#####Teams and hooks not found######
#####deployment empty######
###Rate limiting problem while getting labels####
####Merges url not found#####

#####Code to get all forks#####
url='https://api.github.com/repos/ipython/ipython/forks'
r = requests.get(url)
if r.status_code == 200:
    forks = r.json();
     

    #####Code to get all issues#####
url='https://api.github.com/repos/ipython/ipython/issues'
r = requests.get(url)
if r.status_code == 200:
    issues = r.json();
    
    
    #####Code to get all events#####
url='https://api.github.com/repos/ipython/ipython/events'
r = requests.get(url)
if r.status_code == 200:
    events = r.json();
    
     #####Code to get all assignees#####
url='https://api.github.com/repos/ipython/ipython/assignees'
r = requests.get(url)
if r.status_code == 200:
    assignees = r.json();

    
     #####Code to get all branches#####
url='https://api.github.com/repos/ipython/ipython/branches'
r = requests.get(url)
if r.status_code == 200:
    branches = r.json();
    
    
     #####Code to get all tags#####
url='https://api.github.com/repos/ipython/ipython/tags'
r = requests.get(url)
if r.status_code == 200:
    tags = r.json();
    
    
     #####Code to get all subscribers#####
url='https://api.github.com/repos/ipython/ipython/subscribers'
r = requests.get(url)
if r.status_code == 200:
    subscribers= r.json();
    
    
######Code to get all commits####
url='https://api.github.com/repos/ipython/ipython/commits'
r = requests.get(url)
if r.status_code == 200:
    commits = r.json()
    
    
#####Code to get all comments#####
url='https://api.github.com/repos/ipython/ipython/comments'
r=requests.get(url)
if r.status_code == 200:
    comments = r.json();
    
    #####Code to get all issue comments#####
url='https://api.github.com/repos/ipython/ipython/issues/comments'
r=requests.get(url)
if r.status_code == 200:
    issuecomments = r.json();
    
    
    #####Code to get all Downloads#####
url='https://api.github.com/repos/ipython/ipython/downloads'
r=requests.get(url)
if r.status_code == 200:
   downloads = r.json();
    
   
   
   ###Code to get all Pulls#####
url='https://api.github.com/repos/ipython/ipython/pulls'
r=requests.get(url)
if r.status_code == 200:
   pulls= r.json();
    
   
   ###Code to get all Milestones#####
url='https://api.github.com/repos/ipython/ipython/milestones'
r=requests.get(url)
if r.status_code == 200:
   milestones= r.json();
   
    ###Code to get all Releases#####
url='https://api.github.com/repos/ipython/ipython/releases'
r=requests.get(url)
if r.status_code == 200:
   releases= r.json();
   
   ###Code to get all Gists#####
url='https://api.github.com/users/takluyver/gists'
r=requests.get(url)
if r.status_code == 200:
   gists= r.json();
   
   ###Code to get all Repos#####
url='https://api.github.com/users/ipython/repos'
r=requests.get(url)
if r.status_code == 200:
   repos= r.json();
   
   
    ###Code to get all Events#####
url='https://api.github.com/users/ipython/events'
r=requests.get(url)
if r.status_code == 200:
   events= r.json();
   
   ###Code to get all Received Events#####
url='https://api.github.com/users/ipython/received_events'
r=requests.get(url)
if r.status_code == 200:
   receivedevents= r.json();
   
   
   
   
    
    #for commit in commits:
     #   print(commit['commit']['message']);
        