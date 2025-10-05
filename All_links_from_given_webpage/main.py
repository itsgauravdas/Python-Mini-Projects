import requests
from bs4 import BeautifulSoup
import os

url=input("Entere the url::-")
if("http" or "https") in url:
    data=requests.get(url)
    print(data)
else:
    data = requests.get("https://"+url)
    print(data)
soup = BeautifulSoup(data.text, "html.parser")
links=[]
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Writing the output to a file (myLinks.txt) instead of to stdout
# You can change 'a' to 'w' to overwrite the file each time
os.chdir(os.getcwd()) # Chage the dir to current working directory
with open("my_links.txt",'w') as save:
    if links:
        for i in links:
            save.write(i)
        print("The file is generated and its saved in : -"+ os.getcwd())
    else:
        print("No links found")