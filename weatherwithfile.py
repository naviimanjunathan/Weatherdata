#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Python program to find current 
# weather details of any city
# using openweathermap api
# import required modules
import requests, json
# Enter your API key here
api_key = "05d6694161fcb0b6acea7621170265c5"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# Give city name
city_name = input("Enter city name : ")
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
# get method of requests module
# return response object
response = requests.get(complete_url)
# json method of response object 
# convert json format data into
# python format data
x = response.json()
print(x)
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
    # store the value of "main"
    # key in variable y
    y = x['main']
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
    # store the value corresponding
    # to the "humidity" key of y
    current_humidiy = y["humidity"]
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
    coordinates = x['coord']
    name = x['name']
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z
    weather_description = z[0]["description"]
    # print following values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
    print(str(coordinates))
    print(name)
    f = open("test1.txt",'a+',encoding = 'utf-8')
    f.write("City= "+ str(city_name) + "\n Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)+"\n"+"\n") 
else:
    print(" City Not Found ")


# In[ ]:





# In[ ]:




