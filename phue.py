#This is written for Python3+ so make sure that is the version you are using!
#Python should have the JSON library by default. However the 'requests' library will need to be installed.
#This is pretty dependent and differs for each OS. Linux, for example, is just 'python3 -m pip install requests'
import json, requests

#The URL which is needed for the PUT requests. In this case it is only one light
url='http://192.168.1.242/api/EBV0cft2WAP8HzwVTioBT3uU--HZ3heXjmOdVjnU/lights/1/state'

#Setting the variables for the different colors
redcolor = json.dumps({'hue':2000})
tealcolor = json.dumps({'hue':30000})

#Popping the question
question = input("Do you want a red or teal light? ")

#The requests module is a simple tool for doing PUT requests. Essentially its just requests.put($URLofREQUEST, $BODYINFORMATION)
if question == 'red':
	r = requests.put(url, redcolor)
elif question == 'teal':
	r = requests.put(url, tealcolor)
