"""
Canidate new API for getting weather data from pywapi.
Based on weatherAPI.py

Currently only reports temperature, 
but could be extended to report other information.
"""

import pywapi

class WeatherBase:

    def __init__(self):
        self._celsius_temperature = None

    def update(self):
        """
        This funciton is called to update the weather form the given API.
        Generally, you should not need to call this, unless you want 
        """
        raise NotImplementedError("This must be implemented in the base class")
    
    def temperature(self, using_fahrenheit=True):
        if self._celsius_temperature is None:
            self.update()
        """
        Returns the temperature as of the last update.
        """
        if using_fahrenheit:
            return 1.8 * self._celsius_temperature + 32
        else:
            return self._celsius_temperature



class NOAA(WeatherBase):

    def __init__(self, noaa_city_code='KLAN'):
        super().__init__()
        """
        Creates a new connection to the NOAA API for a given city. 
        :param noaa_city_code: the NOAA city code. This is used to tell NOAA what city we want to look at.
        """
        self.noaa_city_code = noaa_city_code

    def update(self):
        noaa_result = pywapi.get_weather_from_noaa(self.noaa_city_code)
        self._celsius_temperature = float(noaa_result['temp_c'])


class WeatherCom(WeatherBase):

    def __init__(self, zip_code=48912):
        super().__init__()
        self.zip_code = zip_code

    def update(self):
        result = pywapi.get_weather_from_weather_com(str(self.zip_code))['current_conditions']
        self._celsius_temperature = float(result['temperature'])


class Weather(WeatherBase):

    def __init__(self, zip_code=None, noaa_city_code=None):
        super().__init__()
        self.backend = None
        if zip_code is not None:
            self.backend = WeatherCom(zip_code)
        if noaa_city_code is not None:
            self.backend = NOAA(noaa_city_code)
    
    def update(self):
        self.backend.update()
        self._celsius_temperature = self.backend._celsius_temperature

if __name__ == "__main__":
    noaa = NOAA()
    print(noaa.temperature())
    weather_com = WeatherCom()
    print(weather_com.temperature())

    ## New file
    # import weather

    # lansing = NOAA()
    lansing = Weather(noaa_city_code='KLAN')
    print(lansing.temperature())
