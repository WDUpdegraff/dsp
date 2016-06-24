import csv
import urllib.request
import string
from pprint import pprint
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
degreeslist = [None]*(len(biostat)-1)#valuable later
degreestring = ''#using a string to split since there are multiple degrees in each

i=1#to skip first list
while i<len(biostat):
    names[i-1]=biostat[i][0]
    degreeslist[i-1]=biostat[i][1]
    deg = biostat[i][1]
    exclude = set(string.punctuation)
    deg = ''.join(ch for ch in deg if ch not in exclude)
    #killing punctuation so PhD and Ph.D look the same
    degreestring = degreestring+deg+' '
    title=biostat[i][2]
    title = title.replace(' of Biostatistics','')
    title = title.replace(' is Biostatistics','')
    titles[i-1]=title
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
#THIS PRINTS THE ANSWER TO Q1
  
titlenums = countlist(titles)
#print('There are '+str(len(titlenums))+' different titles:')
#print(titlenums)
#THIS PRINTS THE ANSWER TO Q2

#print(emails)
#THIS PRINTS THE ANSWER TO Q3

domainnums = countlist(domains)
print('There are '+str(len(domainnums))+' different domains:')
print(domainnums)
#THIS PRINTS THE ANSWER TO Q4

#THE FOLLOWING CREATES THE CSV FOR Q5
with open('emails.csv', 'w', newline='') as csvfile:
    writeything = csv.writer(csvfile, delimiter = '\n', dialect ='excel')
    writeything.writerow(emails)

surnames =[]
for line in names:
    surnames.append(line[line.rfind(' ')+1:])

surnamesunique = list(set(surnames))

surnamesdict = []
dte = []
faculty_dict = {}

surname = surnamesunique[3] 
for surname in surnamesunique:
    for line in names:
        if surname in line:
            ind = names.index(line)
            fd = [degreeslist[ind],titles[ind],emails[ind]]
            dte.append(fd)
    faculty_dict[surname] = fd 
#pprint(faculty_dict)
#THIS PRINTS THE ANSWER TO Q6

pdict=[None]*len(names)
i=0
while i<len(names):
    toop = tuple(names[i].split())
    pud = [degreeslist[i],titles[i],emails[i]]
    pdict[i] = (toop,pud)
    i=i+1
professor_dict = dict(pdict)
#pprint(professor_dict)
#THIS PRINTS THE ANSWER TO Q7

#pprint(sorted(professor_dict.items(), key=lambda item:item[0][-1]))
#THIS PRINTS THE ANSWER TO Q8
