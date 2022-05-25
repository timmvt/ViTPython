from urllib import response
import requests, json, openpyxl

#assign url to variable
url = "https://motorcycle-specs-database.p.rapidapi.com"

headers = {
    #xrapidHOST
    #xrapidAPI    
}

#check response status to URL
#print response
print[response]
#print content/response.text
clean_data = json.loads(response.text)
#assign response object to variable (json.loads)

#print cleaned data
#print(clean_data)

for i in range(len(clean_data)):
    result = clean_data[1]["name"]
    print(result)
    
    
#create a workbook
wb = openpyxl.Workbook("output.xlsx")

#create a spreadsheet page

#designate columns (loop through columns; change font to bold)

# loop through API data
    #build cell values with appropriate data
    
    
# Save the workbook
