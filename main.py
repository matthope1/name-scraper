import requests
from bs4 import BeautifulSoup

url = input("Enter firstnam.es url: ")

print("getting names from " + url)

html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')

results = soup.find_all("li", "list-item")

filename = input("Enter filename to store names: ")

f = open(filename, "a")

counter = 1

for i in results:
    name = i.find("a")
    f.write('"' + name.text + '",')
    if counter == 10:
        f.write('\n')
        counter = 1

    counter = counter + 1

f.close()


