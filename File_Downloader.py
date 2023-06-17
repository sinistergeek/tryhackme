import requests

print("----Downloading Pic---")

url = 'https://assets.tryhackme.com/img/THMlogo.png'
r = requests.get(url, allow_redirects=True)
print(r)
open('THMlogo.png', 'wb').write(r.content)


print("----Downloading file---")
next_url = 'https://download.sysinternals.com/files/PSTools.zip'
new = requests.get(next_url,allow_redirects=True)
print(r)
open('PSTools.zip','wb').write(new.content)
