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
import yaml

with open('routes.yaml', 'r') as file:
    routes = yaml.safe_load(file)
    


Route1 = routes["Bonfire"]
Route3 = routes["Yell Practice"]
Route4 = routes["Gig Em"]
Route5 = routes["Bush School"]
Route6 = routes["12th man"]
Route8 = routes["Howdy"]

Routes = [Route1, Route3, Route4, Route5, Route6, Route8]


API_KEY = 'AIzaSyA4D8yWsKtga6p5qWkUS_HzwpKbbIjurJI'
geolocator = GoogleV3(api_key=API_KEY)
print(type(geolocator))
gmap = googlemaps.Client(API_KEY)
address = '5307 Belle Manor Ln, Sugar Land, TX 77479'
response = gmap.geocode(address)

current_location = geolocator.geocode("MSC College Station")
#print(current_location)
final_location = geolocator.geocode("Heldenfels Hall")
#print(final_location)
#print(int(gmap.distance_matrix(current_location, final_location, mode='walking')['rows'][0]['elements'][0]['duration']['text'][0]))

def walking_time(currentLocation, finalLocation):
    return int(gmap.distance_matrix(current_location, final_location, mode='walking')['rows'][0]['elements'][0]['duration']['text'][0])

def driving_time(currentLocation, finalLocation):
    return int(gmap.distance_matrix(current_location, final_location, mode='driving')['rows'][0]['elements'][0]['duration']['text'][0])

def closest_stop(currentLocation, route):
    best_time = 10*99
    for stop in route:
        if (walking_time(current_location,stop)<best_time):
            best_time = walking_time(current_location, final_location)
            closest_stop = stop
    return closest_stop

paths = dict()
start_location = "MSC College Station"

def neighboring_locations(start_location)

for Route in Routes:
    for Stop in Route:
        neighboring_locations = []
        closest_stops = []
        for n in Routes:
            neighboring_locations.append((closest_stop(current_stop,n), walking_time(closest_stop(current_location,n))
            paths[Stop] =                                   
                        
            
        
        
# {"MSC": [("Rudder", Time), ()]}
# create dict w bus stop and destination
        
        
        
        
       
        

        


    





'''name = "Memorial Student Center College Station"
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
d = gmap.distance_matrix(p_1, p_2, mode='walking')'''



'''for n in locations:
    print(geolocator.geocode(n))
print(my_locations)
print(d)'''






