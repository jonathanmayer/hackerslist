import requests
import re

print "Project ID\tProject URL\tCreator Username"

projectUrlRe = re.compile(r'a href="/users/login\?f=project/(.*)" title="Place Bid"')
usernameRe = re.compile(r'a href="/messages/compose/user:(.*)/project_id:')

for i in range(1, 7201):

    url = "https://hackerslist.com/projects/project_view_action/pid:" + str(i)
    r = requests.get(url)

    projectUrl = ""
    match = projectUrlRe.search(r.text)
    if match != None:
        projectUrl = match.group(1)

    username = ""
    match = usernameRe.search(r.text)
    if match != None:
        username = match.group(1)

    # Output
    print str(i) + "\t" + projectUrl + "\t" + username