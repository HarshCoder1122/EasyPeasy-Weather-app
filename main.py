#this is the weather app which gives you the basics of weather report for your given city or state or country
import json
import requests
import pyttsx3
engine=pyttsx3.init()
City = input("Enter the city Name: ")
link = f"https://api.weatherapi.com/v1/current.json?key=74cbecd6189d4462ad375827241908&q={City}"#Weather API to get the wheather report
r = requests.get(link) #inbuilt function to run the API
wdic = json.loads(r.text) #convert string to dict by json another inbuilt function

loca= wdic["location"]["name"]     # details which you want to show
locas= wdic["location"]["region"]
count= wdic["location"]["country"]
temp_c = wdic["current"]["temp_c"]
temp_f = wdic["current"]["temp_f"]
alert = wdic["current"]["condition"]["text"]
wind= wdic["current"]["wind_kph"]
humid=wdic["current"]["humidity"]
 
print("City:",loca)  #details which you want to print
print("State:",locas)
print("Country:",count)
print("The Temperature in Celsius:", temp_c)
print("The Temperature in Fahrenheit:", temp_f)
print("Weather:", alert)
print("Wind Speed in Km /H:",wind,)
print("Humidity:",humid)

engine.say(f"City {loca}") #details which you want to speaks
engine.say(f"Sate {locas}")
engine.say(f"Country {count}")
engine.say(f"The temperature in celsius {temp_c} degree celsius")
engine.say(f"The temperature in Fahrenheit {temp_f} degree fahrenheit")
engine.say(f"Weather {alert}")
engine.say(f"Wind speed in kilometer per hour{wind}kilometer per hour")
engine.say(f"humidity {humid}percent")
engine.runAndWait()