# !/usr/bin/python
#
# www.hackthis.co.uk
# coding, level 1
#
# @a: trill
#
import re
import requests

# this must be changed to your cookie info
cookie = {'member':'1', '_ga':'GA1.3.494927184.1435635374', 'autologin':'f%00%13%87%E7%9577%084CP%17%14%2F%88%AE%29%7Cs%10K%BDV%C5%ECP%2F%C5%D1%94ibs%12%7B%F9%FE%F5UVa%2F%EBp%DB%FA%E3kn%11%2F%26%19%E4C%0F%E6%88%7B%D3%60%03%FF', 'PHPSESSID':'1561ernelml5pe4d2rth8ujhs6'}

response = requests.get('https://www.hackthis.co.uk/levels/coding/1', cookies=cookie)

text = re.findall(r'<textarea>[a-z, ]+</textarea>', response.content)

words = text[0].replace(" ", "").split('<textarea>')[1].split('</textarea>')[0]

words1 = words.split(',')

print '[+] Unsorted: '
print words1

words1.sort()

print '[+] Sorted: '
print words1

answer = ", ".join(words1)

# append new cookie info
cookie['_gat'] ='1'

payload = {"answer": answer}
cookies = cookie
r = requests.post('https://www.hackthis.co.uk/levels/coding/1', cookies=cookie, data=payload)
