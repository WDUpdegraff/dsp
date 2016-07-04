import csv
import urllib.request
import string
from pprint import pprint

urlbase = 'https://raw.githubusercontent.com/'
urlrest = 'WDUpdegraff/dsp/master/python/faculty.csv'
url = urlbase+urlrest
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
splitbylines = (response.read().decode('utf-8').splitlines())
biostat = list(csv.reader(splitbylines))

def countlist(rawlist):
    uniques = list(set(rawlist))
    nums = [None]*len(uniques)
    i = 0
    while i < len(uniques):
        nums[i] = [uniques[i],rawlist.count(uniques[i])]
        i = i + 1
    nums.sort(key=lambda x: x[1],reverse = True)
    return nums

names = [None]*(len(biostat)-1)
# minus one because skipping first list
titles = [None]*(len(biostat)-1)
emails = [None]*(len(biostat)-1)
degreeslist = [None]*(len(biostat)-1)# valuable later
degreestring = ''
# populating string to split later since space-delimited

i = 1# to skip first list
while i<len(biostat):
    names[i-1]=biostat[i][0]
    degreeslist[i-1]=biostat[i][1]
    deg = biostat[i][1]
    exclude = set(string.punctuation)
    deg = ''.join(ch for ch in deg if ch not in exclude)
    # killing punctuation so PhD and Ph.D look the same
    degreestring = degreestring+deg+' '
    title=biostat[i][2]
    title = title.replace(' of Biostatistics','')
    title = title.replace(' is Biostatistics','')
    titles[i-1]=title
    emails[i-1]=biostat[i][3]
    i = i + 1

degrees = degreestring.split()
degreeset=set(degrees)
degreeuniques = list(degreeset)

degreenums = [None]*len(degreeuniques)
i = 0
# can't use countlist because I want to filter bad values
while i < len(degreeuniques):
    if any(c.isalpha() for c in degreeuniques[i]) is False:
    # Any degree entry with no letters is 'Unknown Degree'
        a = 'Unknown Degree'
    else:
        a = degreeuniques[i]
    degreenums[i] =[a,degrees.count(degreeuniques[i])]
    i = i + 1

domains = [None]*len(emails)
i = 0
while i < len(emails):
    domains[i] = emails[i][emails[i].find('@') + 1:]
    i = i + 1
    
# Q1:    
degreenums.sort(key=lambda x: x[1],reverse = True)
print('\nQ1:\n')
print('There are ' + str(len(degreeuniques)) + ' types of degrees:\n')
print(degreenums)

# Q2:     
titlenums = countlist(titles)
print('\nQ2:\n')
print('There are ' + str(len(titlenums)) + ' different titles:\n')
print(titlenums)

# Q3:
print('\nQ3:\n')
print(emails)

# Q4:
domainnums = countlist(domains)
print('\nQ4:\n')
print('There are ' + str(len(domainnums)) + ' different domains:\n')
print(domainnums)

# Q5:
with open('emails.csv', 'w', newline= '') as csvfile:
    writeything = csv.writer(csvfile, delimiter = '\n',
                             dialect = 'excel')
    writeything.writerow(emails)

# Q6:
surnames = []
for line in names:
    surnames.append(line[line.rfind(' ') + 1:])

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
print('\nQ6:\n')
pprint(faculty_dict)

# Q7:
pdict = [None]*len(names)
i = 0
while i < len(names):
    toop = tuple(names[i].split())
    pud = [degreeslist[i],titles[i],emails[i]]
    pdict[i] = (toop,pud)
    i = i + 1
professor_dict = dict(pdict)
print('\nQ7:\n')
pprint(professor_dict)

# Q8:
print('\nQ8:\n')
pprint(sorted(professor_dict.items(),
              key=lambda item: item[0][-1]))
