# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:31:12 2023

@author: anaya

"""
from pprint import pprint
import googlemaps
import geopy.distance
from geopy.geocoders import GoogleV3
import pandas as pd

API_KEY = 'AIzaSyA4D8yWsKtga6p5qWkUS_HzwpKbbIjurJI'
geolocator = GoogleV3(api_key=API_KEY)
print(type(geolocator))
gmap = googlemaps.Client(API_KEY)
address = '5307 Belle Manor Ln, Sugar Land, TX 77479'
response = gmap.geocode(address)


name = "Memorial Student Center College Station"
location = geolocator.geocode(name)
print(location.address)
print(location.latitude, location.longitude)

first_location = pd.DataFrame([[name, location.address,location.latitude, location.longitude]], columns = ['name', 'address', 'lat', 'lon'])

name = "Rudder Tower"
location = geolocator.geocode(name)

second_location = pd.DataFrame([[name, location.address,location.latitude, location.longitude]], columns = ['name', 'address', 'lat', 'lon'])
    
my_locations = pd.concat([first_location, second_location], ignore_index= True)

p_1 = (my_locations['lat'][0], my_locations['lon'][0])
p_2 = (my_locations['lat'][1], my_locations['lon'][1])
d = gmap.distance_matrix(p_1, p_2, mode='walking')

print(my_locations)
print(d)






