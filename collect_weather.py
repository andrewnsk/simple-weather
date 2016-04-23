import pyowm
import json
import azimuth

# openweathermap API key
# please use you own api key!
API_KEY = '3ede2418f1124401efcd68e5ae3bddcb'
town = 'Norilsk'
area = 'ru'
owm = pyowm.OWM(API_KEY)

observation = owm.weather_at_place('{0},{1}'.format(town, area))
w = observation.get_weather()
# print(w)


class GetWeather:

    def __init__(self, location, country, owm_api_key):
        self.location = location
        self.country = country
        self.owm_api_key = owm_api_key
        self.owm = pyowm.OWM(owm_api_key)
        self.observation = owm.weather_at_place('{0}{1},ru'.format(self.location, self.country))
        self.w = self.observation.get_weather()

    def wind_direction(self):
        return str(azimuth.degree(round(json.loads(json.dumps(self.w.get_wind()), 1)['deg'])))

    def wind_speed(self):
        return str(round(json.loads(json.dumps(self.w.get_wind()))['speed']))

    def temperature(self):
        return str(round(json.loads(json.dumps(self.w.get_temperature('celsius')))['temp']))

    def humidity(self):
        return int(round(json.loads(json.dumps(self.w.get_humidity()))))


class HumanWeather:

    def __init__(self):
        pass


def get_weather_wind_direction(mode=True):
    return str(azimuth.degree(round(json.loads(json.dumps(w.get_wind()), 1)['deg']), mode))


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
