import requests
import json
import pyttsx3

city = input("Enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=35666ca22ec844f7ade162516231305={city}"

engine = pyttsx3.init()

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

Output = f"The current weather in {city} is {w} degrees"

engine.say(Output)
engine.runAndWait()



