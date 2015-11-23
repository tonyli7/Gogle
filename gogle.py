import json,urllib2, google, bs4, re


["who","when"]
q=input();

def isName(name):
    url="""
    http://dictionaryapi.net/api/definition/%s
    """
    url=url%(str(name[0]))
    request_url = urllib2.urlopen(url)
    result = request_url.read()
    r = json.loads(result)
    if r==[]:
        url="""
        http://dictionaryapi.net/api/definition/%s
        """
        url=url%(str(name[1]))
        request_url = urllib2.urlopen(url)
        result = request_url.read()
        r = json.loads(result)
        if r==[]:
            return True
    return False
    

def getNames(text, dic):
    exp = "[A-Z][a-z]+ [A-Z][a-z]+"
    result = re.findall(exp,text);
    for name in result:
        if name not in dic:
            dic[name]=0;
        dic[name]+=1;

    return dic

def who(namedict):
    test=[]
    for something in namedict:
        test+=[[namedict[something],something]]
    
    test.sort()
    print test
    for name in test[::-1]:
        if isName(name[1].split(" ")):
            return name
    return test[-1][1]

def search(query):
    r = google.search(query,num=10,start=0,stop=10)
    namedict={}
    webnum=0

    for result in r:
        print result
        try:
            u = urllib2.urlopen(result)
            page = u.read()
        except:
            print 'connection error, skipping'
            pass
        soup = bs4.BeautifulSoup(page,"html.parser")
        raw = soup.get_text()
        text = re.sub("[\t\n ]"," ",raw)
        namedict = getNames(text,namedict)
        webnum+=1

    print 'number of websites used: '+str(webnum)
    return who(namedict)


print search(q)
#print isName(["peter","parker"])
