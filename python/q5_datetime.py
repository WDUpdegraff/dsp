# Hint:  use Google to find python function

#days_between can handle any of the three input formats, and more (as seen in the test section)

#Dates must be strings
#Punctuation, whitespace, and capitalization are irrelevant
#The day must be two numerical characters (e.g. '01' not '1' or '001')
#The month must be two numerical characters, or a name containing at least the first three letters of the month
#(e.g. '09' or 'sep' or 'sept' or 'september' or 'septiembre' but not '9' or '009') 
#Year must be the full year; any character length is valid but it will treat '13' as 13 AD

#Dates containing named months can be entered with either EU or US date order (e.g. '15-Jan-1994' or 'January 15, 1994')
#Numerical dates are treated as US order unless EITHER date is only valid in EU order. In that case it assumes BOTH are EU order.
#(e.g. '2-1-2012' is treated as February 1, but '15-1-2012' will be recognized as January 15)
#NOTE IT IS NOT INCLUSIVE -- if date_start = date_stop it returns 0

import math
import string

errmess = "Please enter valid dates not before 1 CE in a consistent format -- mm/dd/yyyy format recommended"

def stringfix(datestring):
    exclude = set(string.punctuation)
    datestring1 = ''.join(ch for ch in datestring if ch not in exclude)
    datestring2 = datestring1.lower()#makes next easier
    datestring2="".join(datestring2.split())
    mons = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    ind = 0
    i = 0
    while i<12:
        if mons[i] in datestring2:
            ind = ind+datestring2.index(mons[i])#this says where you found the month string to tell whether it's European or US format
            if i<9:
                datestring2 = datestring2.replace(mons[i],'0'+str(i+1))
            else:
                datestring2 = datestring2.replace(mons[i],str(i+1))               
        i = i+1
    letters = set(string.ascii_letters)
    datestring3 = ''.join(ch for ch in datestring2 if ch not in letters)#kills any leftover characters for the rest of words
    a = int(datestring3[:2])
    b = int(datestring3[2:4])
    c = int(datestring3[4:])
    if ind>0:#i.e. if the month name string isn't at the beginning so it's a euro date
        return [b,a,c]
    else:
        return [a,b,c]

def leapdays_before(date):#total number of leap days between 1/1/1 and listed date
    if date[2]>0:    
        if date[0]<3 or date[0]==2 & date[1]==29:
            m = date[2]-1
        else:
            m = date[2]
        return math.floor(m/4)-math.floor(m/100)+math.floor(m/400)#This defines how many leap days have elapsed by December 31 on year m (Gregorian Calendar)
    else:
        print (errmess)

def isleap(year):
    ans = [False,True]
    a = (year % 4 == 0)-(year % 100 == 0)+(year % 400 == 0)
    return ans[a]

def nonleap(date):#non leap since we count leaps separately
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]#0 because 0 days completed by start of jan
    check1 = (date[0]-2)
    check2 = (date[1]-29)
    if check1 == 0 and check2 == 0:
 #       if 
        return sum(days[:date[0]])+28
    else:
            return sum(days[:date[0]])+date[1]   

def days_between(date_start,date_stop):
    start = stringfix(date_start)
    finish = stringfix(date_stop)
    if start[0]>12 or finish[0]>12:#if the month alone is over twelve, it assumes the date is EU style and switches month with day
        start = [start[1],start[0],start[2]]
        finish = [finish[1],finish[0],finish[2]]#recognizes date is european
    if start[0]>12 or finish[0]>12:#if the month is still>12 even euro style
        return errmess
    if start[0]==2 and start[1]==29:
        if isleap(start[2]) == False:
            print(str(start[2])+" is not a leap year. "+errmess)
    if finish[0]==2 and finish[1]==29:
        if isleap(finish[2]) == False:
            print(str(finish[2])+" is not a leap year. "+errmess)       
    leaps = leapdays_before(finish)-leapdays_before(start)
    nonleaps = nonleap(finish) - nonleap(start)
    years = 365*(finish[2]-start[2])
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    message = 'There were ' +str(leaps+nonleaps+years)+' days between '+ months[start[0]-1]+ ' ' +str(start[1]) + ', ' +str(start[2])+ ' CE and '+ months[finish[0]-1]+ ' ' +str(finish[1]) + ', ' +str(finish[2])+ ' CE.'
    print(message)

#tests

#days_between('01/02/2013','07/28/2015')#should be 937
#days_between('12312013','05282015')#should be 513
#days_between('15-Jan-1994','14-Jul-2015')#should be 7850
#days_between('January 15, 1994','July 14, 2015')#should be 7850
#days_between('July 14, 2015','January 15, 1994')#should be -7850
#days_between('January 15, 1994','07142015')#should be 7850
#days_between('02-15-1999','03-12-1999')#should be 25
#days_between('15-02-1999','12-03-1999')#should be 25
#days_between('02/28/2000','03/01/2000')#should be 2
#days_between('02/28/1900','03/01/1900')#should be 1 since 1900 isn't a leap year
#days_between('02/29/1900','07/28/2015')#should give error

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

Output: There were 937 days between January 2, 2013 CE and July 28, 2015 CE.

####b)  
date_start = '12312013'  
date_stop = '05282015'  

Output: There were 513 days between December 31, 2013 CE and May 28, 2015 CE.

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

Output: There were 7850 days between January 15, 1994 CE and July 14, 2015 CE.
