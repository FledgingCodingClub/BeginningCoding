import json, requests

url='http://192.168.1.242/api/EBV0cft2WAP8HzwVTioBT3uU--HZ3heXjmOdVjnU/lights/1/state'

redcolor = json.dumps({'hue':2000})
tealcolor = json.dumps({'hue':30000})

question = input("Do you want a red or teal light? ")

if question == 'red':
	r = requests.put(url, redcolor)
elif question == 'teal':
	r = requests.put(url, tealcolor)
