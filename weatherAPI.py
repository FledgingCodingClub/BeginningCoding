# weatherAPIExample.py

## This code gets weather condition and temperature for a city given by the user.
## I used python version 3.6.3.
## Has a depenency on python-weather-api found at https://code.google.com/archive/p/python-weather-api/.

# import the python-weather-api
import pywapi

# function to convert Celsius to Fahrenheit
def celsiusToFahrenheit(c):
    f = 1.8 * c + 32
    return str(f)

# looks up the codes for a city
def lookUpCityCode(s):
    if str(s) == "Lansing":
        noaa_code = "KLAN"
        zip_code = "48912"
    else:
        print("Sorry, the weather for that city is unavailable.")
        noaa_code = 0
        zip_code = 0
    
    return noaa_code, zip_code

def main():
    # prompt the user for a city
    user_input = input("Please input a city: ")
    # look up the code for that city
    noaa_code, zip_code = lookUpCityCode(user_input)

    # if the city is known, find the weather data
    if (noaa_code + zip_code):
        # gather data from both weather.com and noaa
        weather_com_result = pywapi.get_weather_from_weather_com(zip_code)
        noaa_result = pywapi.get_weather_from_noaa(noaa_code)
        
        # convert the weather.com temp from C to F
        weather_com_temp = celsiusToFahrenheit(float(weather_com_result['current_conditions']['temperature']))
        
        # output the results
        print ("Weather.com says the weather in "+ user_input + " is " + weather_com_result['current_conditions']['text'].lower() + " and the temperature is " + weather_com_temp + " F (" + weather_com_result['current_conditions']['temperature'] + " C).")

        print ("NOAA says the weather in "+ user_input + " is " + noaa_result['weather'].lower() + " and the temperature is " + noaa_result['temperature_string'] + ".")

main()
