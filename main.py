import urllib
import requests

key = '<YOUR API KEY>' # Put your API Key
url = urllib.parse.quote('<URL YOU WANT TO SHORT>')
name  = '<CUSTOM ALIAS>'
userDomain = '0' # 0 = Use "cuttl.ly" as the domain. 1 = Use your custom domain
r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}&userDomain={}'.format(key, url, name, userDomain))
print(r.text) # Print response from API

# https://cutt.ly/ (This isn't an affialiate link)