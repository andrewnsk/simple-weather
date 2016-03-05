import pyowm
import json
import azimuth

# openweathermap API key
owm = pyowm.OWM('3ede2418f1124401efcd68e5ae3bddcb')
# Town
observation = owm.weather_at_place('Norilsk,ru')
w = observation.get_weather()
print(w)


def weather_wind():
    return "Ветер: " + str(azimuth.degree(round(json.loads(json.dumps(w.get_wind()), 1)['deg'])) + " " +
                           str(round(json.loads(json.dumps(w.get_wind()))['speed'])) + " м/с")


def weather_temp():
    return "Температура: " + str(round(json.loads(json.dumps(w.get_temperature('celsius')))['temp']))


def weather_humidity():
    return "Влажность: " + str(round(json.loads(json.dumps(w.get_humidity())))) + " %"
