import re
import urllib.request

def transform(source):
    '''
    transform lyrics into the form that MediaGo can read
    '''
    result=[]
    for line in source:
        if bool(re.search(r'\[\d\d.\d\d.\d\d\d\]',line)):
            res=line[:9]+line[10:]
            result.append(res)
        else :
            result.append(line)
    return result

def fetch(id):
    result=[]
    url="http://music.163.com/api/song/media?id="+str(id)
    response=urllib.request.urlopen(url)
    html = response.read()
    return html.decode('utf-8')
    #return result

# test fetch
id=input("请输入网易歌曲id:")
res=fetch(id)
import json
res_dict = json.loads(res)
list_res=res_dict["lyric"].split('\n')
#print(list_res)
trans_res=transform(list_res)
for line in trans_res:
    print(line)
