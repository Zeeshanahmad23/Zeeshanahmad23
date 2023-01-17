# Zeeshan Ahmad


import requests
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
api_key = "Vh6nI66uiHLekXVtVU4sfMaN91MD2xjybYyh19xf"
start_date = "2022-01-12"
end_date = "2022-01-13"
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
print(url)

r = requests.get(url)

data = r.json()
pprint(data)

total = data["element_count"]
pprint(total)

neo = data["near_earth_objects"]
pprint(neo)

first = neo["2022-01-13"][0]
pprint(first)



all_asteroids = neo[start_date]
for asteroid in all_asteroids:
    if asteroid["name"] == "(2022 AS3)":
        pprint(asteroid)
        break
my_name = asteroid["name"]
pprint(my_name)
my_id = asteroid["id"]
pprint(my_id)
my_url = asteroid["nasa_jpl_url"]
pprint(my_url)
my_lum = asteroid["absolute_magnitude_h"]   #luminosity
pprint(my_lum)
my_dia = asteroid["estimated_diameter"]
pprint(my_dia)
my_sen = asteroid["is_potentially_hazardous_asteroid"]
pprint(my_sen)
close_data = asteroid["close_approach_data"]
pprint(close_data)
miss_distance = close_data[0]["miss_distance"]
pprint(miss_distance)
rel_vel = close_data[0]["relative_velocity"]
pprint(rel_vel)




    
     

      
  
 
  