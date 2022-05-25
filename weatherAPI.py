import json, requests, webbrowser

weatherURL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"

weatherAPIRequest = requests.get(weatherURL)

weatherPullRequest = json.loads(weatherAPIRequest)

weatherResults = weatherPullRequest['']