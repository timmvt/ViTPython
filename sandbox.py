import webbrowser
import requests
import bs4

#webbrowser.open('https://inventwithpython.com/')

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(type(res))

print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:250])

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')

elems = exampleSoup.select('#author')

print(type(elems)) # elems is a list of Tag objects.


