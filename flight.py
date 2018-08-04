import json
import requests

api_key = "AIzaSyCxC53nAkMaeEDWFCmCT8JXOA8Qcv8ej0g"
url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
headers = {'content-type': 'application/json'}

origin = "MSY"
destination = "ATL"
date = "2016-12-10"
maxPrice = "USD300"
earliestTime = ""
latestTime = ""

params = {
  "request": {
    "slice": [
      {
        "origin": origin,
        "destination": destination,
        "date": date,
        "permittedDepartureTime": {
          "earliestTime": earliestTime,
          "latestTime": latestTime
        }
      }
    ],
    "passengers": {
      "adultCount": 1
    },
    "solutions": 20,
    "maxPrice": maxPrice,
    "refundable": False
  }
}

response = requests.post(url, data=json.dumps(params), headers=headers)
data = response.json()

minTime = 0
minPrice = 0
for j in range(1, len(data['trips']['tripOption'])):
    PriceOld = data['trips']['tripOption'][minPrice]['saleTotal']
    PriceNew = data['trips']['tripOption'][j]['saleTotal']
    PriceOld = PriceOld[3:]
    PriceNew = PriceNew[3:]
    if float(PriceNew) < float(PriceOld):
        minPrice = j
    
    if int(data['trips']['tripOption'][j]['slice'][0]['duration']) < int(data['trips']['tripOption'][minTime]['slice'][0]['duration']):
        minTime = j


print ("Solution with minimum time:")
print ('Sale Total', data['trips']['tripOption'][minTime]['saleTotal'])
print ('Time Total', data['trips']['tripOption'][minTime]['slice'][0]['duration'])
for i in range(0, len(data['trips']['tripOption'][minTime]['slice'][0]['segment'])):
    print (data['trips']['tripOption'][minTime]['slice'][0]['segment'][i]['flight']['carrier'],
           data['trips']['tripOption'][minTime]['slice'][0]['segment'][i]['flight']['number'],
           data['trips']['tripOption'][minTime]['slice'][0]['segment'][i]['leg'][0]['origin'],
           data['trips']['tripOption'][minTime]['slice'][0]['segment'][i]['leg'][0]['departureTime'],
           data['trips']['tripOption'][minTime]['slice'][0]['segment'][i]['leg'][0]['destination'],
           data['trips']['tripOption'][minTime]['slice'][0]['segment'][i]['leg'][0]['arrivalTime'])
print ("")

print ("Solution with minimum time:")
print ('Sale Total', data['trips']['tripOption'][minPrice]['saleTotal'])
print ('Time Total', data['trips']['tripOption'][minPrice]['slice'][0]['duration'])
for i in range(0, len(data['trips']['tripOption'][minPrice]['slice'][0]['segment'])):
    print (data['trips']['tripOption'][minPrice]['slice'][0]['segment'][i]['flight']['carrier'],
           data['trips']['tripOption'][minPrice]['slice'][0]['segment'][i]['flight']['number'],
           data['trips']['tripOption'][minPrice]['slice'][0]['segment'][i]['leg'][0]['origin'],
           data['trips']['tripOption'][minPrice]['slice'][0]['segment'][i]['leg'][0]['departureTime'],
           data['trips']['tripOption'][minPrice]['slice'][0]['segment'][i]['leg'][0]['destination'],
           data['trips']['tripOption'][minPrice]['slice'][0]['segment'][i]['leg'][0]['arrivalTime'])
print ("")
