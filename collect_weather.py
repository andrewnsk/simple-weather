import pyowm
import json
import azimuth

# openweathermap API key
# please use you own api key!
api_key = '3ede2418f1124401efcd68e5ae3bddcb'
town = "Norilsk"
owm = pyowm.OWM(api_key)

observation = owm.weather_at_place('{0},ru'.format(town))
w = observation.get_weather()
# print(w)


class GetWeather:

    def __init__(self, location, owm_api_key):
        self.location = location
        self.owm_api_key = owm_api_key
        self.owm = pyowm.OWM(owm_api_key)
        self.observation = owm.weather_at_place('{0},ru'.format(self.location))
        self.w = self.observation.get_weather()

    def get_wind_direction(self):
        return str(azimuth.degree(round(json.loads(json.dumps(self.w.get_wind()), 1)['deg'])))


def get_weather_wind_direction():
    return str(azimuth.degree(round(json.loads(json.dumps(w.get_wind()), 1)['deg'])))


def get_weather_wind_speed():
    return str(round(json.loads(json.dumps(w.get_wind()))['speed']))


def get_weather_temperature():
    return str(round(json.loads(json.dumps(w.get_temperature('celsius')))['temp']))


def get_weather_humidity():
    return int(round(json.loads(json.dumps(w.get_humidity()))))


def weather_wind():
    return "Ветер: " + get_weather_wind_direction() + " " + get_weather_wind_speed() + " м/с"


def weather_temp():
    return "Температура: " + get_weather_temperature()


def weather_humidity():
    return "Влажность: " + str(get_weather_humidity()) + " %"
