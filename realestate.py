from bs4 import BeautifulSoup
import requests, openpyxl, json

url = 'https://www.zillow.com/homes/Park-Slope,-New-York,-NY_rb/'
page = requests.get(url)
# print(page)
price_list = json.loads(page.text)
results = price_list['prices']
print(results)

# soup = BeautifulSoup(page.content, 'html.parser')

# #lists = soup.findall('', class_='')
# prices = soup.find_all('div', class_='list-card-price')

# for i in range (len(prices)):
#     print(price[i].text)