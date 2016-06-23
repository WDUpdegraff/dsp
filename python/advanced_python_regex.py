#Didn't use regex because more familiar with this approach

import csv
import urllib.request
import string
url = 'https://raw.githubusercontent.com/WDUpdegraff/dsp/master/python/faculty.csv'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
splitbylines = (response.read().decode('utf-8').splitlines())
biostat = list(csv.reader(splitbylines))

def countlist(rawlist):#relevant later
    uniques = list(set(rawlist))
    nums = [None]*len(uniques)
    i=0
    while i<len(uniques):
        nums[i]=[uniques[i],rawlist.count(uniques[i])]
        i=i+1
    nums.sort(key=lambda x: x[1],reverse = True)
    return nums

names = [None]*(len(biostat)-1)#because skipping first list
titles = [None]*(len(biostat)-1)
emails = [None]*(len(biostat)-1)
degreestring = ''#using a string to split since there are multiple degrees in each

i=1#to skip first list
while i<len(biostat):
    names[i-1]=biostat[i][0]
    deg = biostat[i][1]
    exclude = set(string.punctuation)
    deg = ''.join(ch for ch in deg if ch not in exclude)
    #killing punctuation so PhD and Ph.D look the same
    degreestring = degreestring+deg+' '
    titles[i-1]=biostat[i][2]
    emails[i-1]=biostat[i][3]
    i=i+1

degrees = degreestring.split()
degreeset=set(degrees)
degreeuniques = list(degreeset)

degreenums = [None]*len(degreeuniques)
i=0
while i<len(degreeuniques):#didn't use countlist because of the filtering in the next line
    if any(c.isalpha() for c in degreeuniques[i])==False:
    #if there are no letters in a degree entry, call it an unknown degree
        a = 'Unknown Degree'
    else:
        a = degreeuniques[i]
    degreenums[i] =[a,degrees.count(degreeuniques[i])]
    i=i+1

domains = [None]*len(emails)
i=0
while i<len(emails):
    domains[i] = emails[i][emails[i].find('@')+1:]
    i=i+1
    
degreenums.sort(key=lambda x: x[1],reverse = True)#the next two lines print the answer to Q1
#print('There are '+str(len(degreeuniques))+' types of degrees:')
#print(degreenums)  
  
titlenums = countlist(titles)#the next two lines print the answer to Q2
#print('There are '+str(len(titlenums))+' different titles:')
#print(titlenums)

#the next two lines print the answer to Q3
#emailsprint = sorted(emails)
#print(emailsprint)

domainnums = countlist(domains)#the next two lines print the answer to Q4
#print('There are '+str(len(domainnums))+' different domains:')
#print(domainnums)
