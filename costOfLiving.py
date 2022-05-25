import requests

locationurl = "https://cities-cost-of-living1.p.rapidapi.com/get_cities_list"
weatherurl = "https://weatherapi-com.p.rapidapi.com/ip.json"

querystring = {"q":"<REQUIRED>"}

locationHeaders = {
	"X-RapidAPI-Host": "cities-cost-of-living1.p.rapidapi.com",
	"X-RapidAPI-Key": "4ed1925692msh2967c9c386ba738p185835jsn6e8c696f296e"
}

weatherHeaders = {
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
	"X-RapidAPI-Key": "4ed1925692msh2967c9c386ba738p185835jsn6e8c696f296e"
}

weatherResponse = requests.request("GET", weatherurl, headers=weatherHeaders, params=querystring)
locationResponse = requests.request("GET", locationurl, headers=locationHeaders)
print(weatherResponse.text)

print(weatherResponse.text)
print(locationResponse.text)