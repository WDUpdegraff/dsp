# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import urllib.request
url = 'https://raw.githubusercontent.com/WDUpdegraff/dsp/master/python/football.csv'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
splitbylines = (response.read().decode('utf-8').splitlines())
football = list(csv.reader(splitbylines))


GA = football[0].index('Goals Allowed')
G = football[0].index('Goals')
T = football[0].index('Team')#indices in each list with desired values

diff = [None]*(len(football)-1)#create empty list to populate with differences

i=1#to skip first col
while i<len(football):
    diff[i-1]=abs(int(football[i][G])-int(football[i][GA]))
    i=i+1

ind = diff.index(min(diff))+1#+1 to account for the entry with column names
team = football[ind][T]
print(team+' was the team with the smallest difference in ‘for’ and ‘against’ goals.')

