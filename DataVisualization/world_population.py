import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
from pygal.style import RotateStyle as rs
from pygal.style import LightColorizedStyle as lcs


filename = 'data/population_data.json'
with open(filename) as f:
    populations = json.load(f)


def get_country_code(country_name):
    for code, country in COUNTRIES.items():
        if country == country_name:
            return code

# cc_populations = {}
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for pop_dict in populations:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        country_code = get_country_code(country_name)
        population = int(float(pop_dict['Value']))
        if country_code is not None:
            # cc_populations[country_code] = population
            if population < 10000000:
                cc_pop_1[country_code] = population
            elif population < 1000000000:
                cc_pop_2[country_code] = population
            else:
                cc_pop_3[country_code] = population

wm_style = rs('#336699', base_style=lcs)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Populations in 2010'
# wm.add('2010', cc_populations)
wm.add('less than 10m', cc_pop_1)
wm.add('10m to 1bn', cc_pop_2)
wm.add('more than 1bn',cc_pop_3)
wm.render_to_file('world_populations.svg')
   
