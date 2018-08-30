## include callWeather Funtion to get the Current Temp of City Code Passed ##

import callWeather

## Create Target City's Variable and set Current Temp ##
LansingTemp = callWeather.currentTemp('KLAN')

## Logic Flow ##

if LansingTemp >= 75:
    changeLight('BLUE')

else:
    changeLight('RED')
