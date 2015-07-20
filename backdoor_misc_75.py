#!/usr/bin/python
#
# backdoor.sdslabs.co
# 2013-misc-75
#
# author: trill
import re
import requests

response = requests.get('http://hack.bckdr.in/2013-MISC-75/misc75.php')
numbers = re.findall(r'\d+', str(response.content))
cookie = response.cookies['PHPSESSID']

number = int(numbers[1])
total = 0
x = 1
i = 2
while x <= number:
    flag = True
    for y in range(2, i):
		if i % y == 0:
			flag = False
			break
	    
		if flag == True:
			total += i
			x += 1
    i += 1

payload = {"answer": str(total)}
cookies = dict(PHPSESSID=str(cookie))
r = requests.post('http://hack.bckdr.in/2013-MISC-75/misc75.php', cookies=cookies, data= {"answer": str(total)})
print r.content
