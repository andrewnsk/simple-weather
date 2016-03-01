from mako.template import Template
from mako import exceptions as except_mako
from collect_weather import weather_wind

wind = str(weather_wind())
try:
    def render_tpl():
        mytemplate = Template(filename='./tpl/weather.tpl')
        return mytemplate.render()
except:
    print(except_mako.text_error_template().render())