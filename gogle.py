import urllib2, google, bs4, re


["who","when"]
q=input();

def who(text):
    namedict={}
    exp = "[A-Z][a-z]+ [A-Z][a-z]+"
    result = re.findall(exp,text);
    for name in result:
        if name not in namedict:
            namedict[name]=0;
        namedict[name]+=1;

    test=[]
    for something in namedict:
        test+=[[namedict[something],something]]
    
    test.sort()
    return test[len(test)-1][1]

def search(query):
    r = google.search(query,num=10,start=0,stop=10)
    l=[]
    for result in r:
        l.append(result)

    print "this is the length:"+str(len(l))

    u = urllib2.urlopen(l[0])
    page = u.read()
    #print page
    soup = bs4.BeautifulSoup(page,"html.parser")
    raw = soup.get_text()
    #print raw
    text = re.sub("[\t\n ]"," ",raw)
    
    return who(text)


    
print search(q)
