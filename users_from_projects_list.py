import requests
import re

print "Username\tApp-Specific Facebook ID"

userRe = re.compile(r'<a href="/user/.*?</span></span></a>', re.DOTALL)
userNameRe = re.compile(r'<a href="/user/(.*?)" class="span top-smspace no-mar ver-space">')
fbRe = re.compile(r'<img src="//graph\.facebook\.com/(.*?)/picture\?type=normal')

cookies = {"PHPSESSID": ""}

for i in range(1, 229):

	url = "https://hackerslist.com/projects/index/page:" + str(i)
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
