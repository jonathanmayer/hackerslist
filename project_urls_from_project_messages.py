import requests
import re

print "Project ID\tProject URL"

projectUrlRe = re.compile(r'<dt>Name</dt>\n<dd> <a href="/project/(.*?)" title="')

cookies = {"PHPSESSID": ""}

for id in range(1, 7201):

    projectUrl = ""

    try:
        url = "https://hackerslist.com/messages/index/project_id:" + str(id)
        r = requests.get(url, cookies = cookies, timeout = (1.0, 5.0))

        match = projectUrlRe.search(r.text)
        if match != None:
            projectUrl = match.group(1)
    except:
        pass

    # Output
    print str(id) + "\t" + projectUrl