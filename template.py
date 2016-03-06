from mako.template import Template
from mako import exceptions as except_mako
from collect_weather import weather_wind

wind = str(weather_wind())
try:
    def render_tpl():
        my_template = Template(filename='./tpl/weather.tpl')
        return my_template.render()
except:
    print(except_mako.text_error_template().render())