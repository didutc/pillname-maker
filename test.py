import requests
import doubleagent
import webbrowser
num = '20408'


t = requests.get(
    'http://www.msgood4u.com/html/search/search.php?skey=all&directsearch=y&searchTerm=&sword='+str(num)+'').text
t = t.split('line_4')[1:]
print(len(t))

for li in t:
    lnum = li.split('상품코드 <span>')[1:][0]
    lnum = lnum.split('</span>')[0]
    if num == lnum:
        target = li
        break
img = target.split("<img src='")[1:][0].split(' ')[0]
if not "http" in img:
    img = 'http://www.msgood4u.com/'+img
link = target.split("<a href='")[1:][0].split("'")[0]
print(img,link)