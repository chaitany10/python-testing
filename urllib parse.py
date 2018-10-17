import urllib.request
import urllib.parse

'''
url = 'http://www.pythonprogramming.net'
values={'s':'basic','submit':'search'}

#=urllib.request.urlopen("https://google.com")
data = urllib.parse.urlencode(values)
#print(link.read())
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData=resp.read()

print(respData)
'''
try:
    x=urllib.request.urlopen('https://www.google.com/search?q=test')

    print(x.read())

except Exception as e:
    print(str(e))

try:
    url=urllib.request.urlopen('https://www.google.com/search?q=test')

    header ={}
    header['User-Agent']= 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url,headers=header)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    savefile = open('withheaders.txt','w')
    savefile.write(str(respData))
    savefile.close()

except Exception as e:
    print(str(e))