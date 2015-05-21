import requests
import re

print "Username\tApp-Specific Facebook ID"

userRe = re.compile(r'<div class="pull-left clearfix top-space"> <span class="pr"><span class="avtar-box pull-left pr mob-clr">.*?img-rounded img-polaroid".*?"/></a></span></span> </div>', re.DOTALL)
userNameRe = re.compile(r'<a href="/user/(.*?)" title="')
fbRe = re.compile(r'<img src="//graph\.facebook\.com/(.*?)/picture\?type=normal')

cookies = {"PHPSESSID": ""}

for i in range(1, 131):

	url = "https://hackerslist.com/users/index/page:" + str(i)
	r = requests.get(url, cookies = cookies)

	for match in userRe.finditer(r.text):
		inner = match.group(0)
		userMatch = userNameRe.search(inner)
		if userMatch != None:
			user = userMatch.group(1)
			fb = ""
			fbMatch = fbRe.search(inner)
			if fbMatch != None:
				fb = fbMatch.group(1)
			print user + "\t" + fb
