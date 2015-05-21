import requests
import re

print "Project ID\tLast Revision Time\tLast Revision Name\tLast Revision Location\tLast Revision Budget\tLast Revision Description"

timeRe = re.compile(r'<span class="c" title="(.*)">')
nameRe = re.compile(r'<span class="c(1)?">(.*)</span>')
addressRe = re.compile(r'<td>(<span class="c">)?(.*?)(</span>)?</td>')
amountRe = re.compile(r'<span class="c">(.*)</span>')
descriptionRe = re.compile(r'<td colspan="13"><p class="js-truncate {\'len\':\'350\'}">(.*?)</p></td>', flags=re.DOTALL)

cookies = {"PHPSESSID": ""}

for i in range(1, 7201):

    url = "https://hackerslist.com/revisions/index/" + str(i) + "/project"
    r = requests.get(url, cookies = cookies)

    time = ""
    match = timeRe.search(r.text)
    next = 0
    if match != None:
        time = match.group(1)
        next = next + match.end()

    name = ""
    match = nameRe.search(r.text[next:])
    if match != None:
        name = match.group(2)
        next = next + match.end()

    address = ""
    match = addressRe.search(r.text[next:])
    if match != None:
        address = match.group(2)
        next = next + match.end()

    amount = ""
    match = amountRe.search(r.text[next:])
    if match != None:
        amount = match.group(1)
        next = next + match.end()

    description = ""
    match = descriptionRe.search(r.text[next:])
    if match != None:
        description = match.group(1).replace("\n", " ").replace("\t", " ").strip()

    print str(i) + "\t" + time + "\t" + name + "\t" + address + "\t" + amount + "\t" + description