import re

def getDates(text, dic):
    """
    [A-Z,0-9][a-z,0-9]*: Handles if the first word starts with a capital letter
                         followed by lowercase, OR if the first word is a number
                         representing the month/day

    [.,/, ]? ?:          Handles characters following the first word. Includes
                         slashes(/), periods(.), and spaces( ). It also handles
                         the case when there is a space following it.

    [A-Z,0-9][a-z,0-9]*: Similar to above for instances like 19 October 2014

    [,,/, ] ?:           Similar to above

    ?[0-9]{2,4}:         Handles the year, restricting it from 2-4 characters

    
    """
    exp="[A-Z,0-9][a-z,0-9]*[.,/, ]? ?[A-Z,0-9][a-z,0-9]*[,,/, ] ?[0-9]{2,4}"
    result = re.findall(exp,text);
    for name in result:
        if name not in dic:
            dic[name]=0;
        dic[name]+=1;

    return dic

def when(namedict):
    test=[]
    for something in namedict:
        test+=[[namedict[something],something]]
    
    test.sort()
    print test
    return test[-1][1]

#print when("October 19, 14")
#print when("11/10/14")
#print when("Oct. 19 2014")
#print when("19 October 2014")
