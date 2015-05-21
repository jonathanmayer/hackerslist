import requests
import re

print "Project ID\tContact Information"

cookies = {"PHPSESSID": ""}

for id in range(1, 7201):
	email = ""
	try:
		# Fetch email
		url = "https://hackerslist.com/projects/show_contact_info/" + str(id)
		r = requests.get(url, cookies = cookies)

		email = r.text.strip().replace("\n", " ")
	except:
		pass

	# Output
	print str(id) + "\t" + email