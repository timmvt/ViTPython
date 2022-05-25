import json, requests

url = "https:/api.openweathermap.org/data/2.5/weather"
api_key = "ed0652b5563cf9225a46a6ad8c2fa9dc"

city_name = input("What city do you want to find? ")
city_country = input("What country is that city in? ")

url_string = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{city_country}&units=imperial&appid={api_key}"
res = requests.get(url_string)
parsed_data = json.loads(res.text)

weather = parsed_data['weather'][0]
weather_description = weather["description"]
main = parsed_data["main"]
main_temp = main["temp"]
celsius = round(float((main_temp - 32) * 0.5556),2)
#main_temp_feels = main["feels like"]

print(f"Today in {city_name}")
print(f"It's {main_temp} and {weather_description}")
print(f"In celsius {celsius} and still {weather_description}")
#print(f"but it feels like {main_temp_feels}")