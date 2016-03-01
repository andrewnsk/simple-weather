## -*- coding: utf-8 -*-
<html>
${wind}
${temp}
${hum}
</html>

<%!
from collect_weather import weather_wind, weather_temp, weather_humidity
wind = str(weather_wind())
temp = str(weather_temp())
hum = str(weather_humidity())
%>
