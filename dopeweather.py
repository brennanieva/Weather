#Author: Brenna Nieva
#Date: 10/14/2019
#Description:

#Version 2
import requests
import json

# Enter your API key here
api_key = "19e591d87e7c406e17b46b8f0d9c6e1d"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
zip_code = input("Enter zip code : ")

# complete url address
complete_url = base_url + "appid=" + api_key + "&zip=" + zip_code

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

#as long as a city is found, gather the temperature and description data
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    #Snatch the current temp (automatically in kelvin) and convert it to F
    current_temperature = y["temp"]
    FTemp = int(current_temperature * 9/5 - 459.67)

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print("The temperature is %s .  You can expect the weather outside to be %s" %(FTemp,weather_description))

else:
    print(" City Not Found ")

sunnycloudy = input("Is it sunny or cloudy outside? ")

#Its sunny outside and checks the user's temperature
if sunnycloudy.lower() == "sunny":
    if  FTemp   < 60:
        clothes = "Wear a sweater"
    elif FTemp == 60:
        clothes = "60 degrees is the magic temperature, you can wear whatever you want"
    else:
        clothes = "Flip flops and a tshirt bro"
    print(clothes)
#Its cloudy outside and checks the user's temperature
if sunnycloudy.lower() == "cloudy":
    if FTemp < 40:
        clothes = "Wear a coat and hat. its cold"
    elif FTemp > 40 and FTemp < 50:
        clothes = "Not quite freezing but close, bundle up"
    elif FTemp == 50:
        clothes = "Wear a jacket"
    else:
        clothes = "Wear a long sleeved shirt"
    print(clothes)
