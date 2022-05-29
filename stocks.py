from ctypes.wintypes import CHAR
from openpyxl import Workbook
from openpyxl import load_workbook
import json   # imports json
import requests   # imports requests

# Access an API
url = "https://alpha-vantage.p.rapidapi.com/query"

# Open Workbook
wb = load_workbook("stocks.xlsx")
stockSheetNames = wb.get_sheet_names()

querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"compact"}

headers = {
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
	"X-RapidAPI-Key": "4ed1925692msh2967c9c386ba738p185835jsn6e8c696f296e"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)