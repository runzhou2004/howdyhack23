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

Routes = {"Route1":Route1, "Route3":Route3, "Route4":Route4, "Route5":Route5, "Route6":Route6, "Route8":Route8}


API_KEY = 'AIzaSyA4D8yWsKtga6p5qWkUS_HzwpKbbIjurJI'
geolocator = GoogleV3(api_key=API_KEY)
print(type(geolocator))
gmap = googlemaps.Client(API_KEY)
address = '5307 Belle Manor Ln, Sugar Land, TX 77479'
response = gmap.geocode(address)

#current_location = geolocator.geocode("MSC College Station")
#print(current_location)
#final_location = geolocator.geocode("Heldenfels Hall")
#print(final_location)
#print(int(gmap.distance_matrix(current_location, final_location, mode='walking')['rows'][0]['elements'][0]['duration']['text'][0]))

def walking_time(current_location, final_location):
    return int(gmap.distance_matrix(current_location.split(',',1)[1], final_location.split(',',1)[1], mode='walking')['rows'][0]['elements'][0]['duration']['text'].split(' ',1)[0])

def driving_time(current_location, final_location):
    return int(gmap.distance_matrix(current_location.split(',',1)[1], final_location.split(',',1)[1], mode='driving')['rows'][0]['elements'][0]['duration']['text'].split(' ',1)[0])

#print(gmap.distance_matrix('503 George Bush Dr W, College Station, TX 77840',"212 Adriance Lab Rd, College Station, TX 77843", mode='walking')['rows'][0]['elements'][0]['duration']['text'])
#print(walking_time('503 George Bush Dr W, College Station, TX 77840',"212 Adriance Lab Rd, College Station, TX 77843"))

def closest_stop(current_location, route):
    best_time = 10**99
    closest_stops = []
    for stop in route:
        '''print(stop)
        print(walking_time(current_location,stop))
        print(best_time)
        print(closest_stops)'''
        if (walking_time(current_location,stop) < best_time):
            best_time = walking_time(current_location,stop)
            closest_stops = [stop]
        elif(walking_time(current_location,stop)== best_time):
            closest_stops.append(stop)
            
    return closest_stops

#print(walking_distance("School of Public Health, 212 Adriance Lab Rd, College Station, TX 77843", ))

#print(closest_stop("School of Public Health, 212 Adriance Lab Rd, College Station, TX 77843", Route8))
#print(walking_time("1000 MSRB Dr, College Station, TX 77845", "NCTM, 100 Discovery Dr, College Station, TX 77845"))



paths = dict()
start_location = "MSC College Station"


'''def closest_stops(location):
    closest_stops = []
    for n in Routes:
        closest_stops.append((closest_stop(location,n),walking_time(location, closest_stop(location,n))))
    return closest_stops'''

'''
#print(closest_stops("MSC College Station"))

#print(walking_time("MSC college station", "Ross Street & Bizzell Street, College Station, TX 77840"))

def time_to_stops(location):
    stops = []
    for route in Routes:
        for i in route:
            stops.append((i, walking_time(location.split(',',1)[1],i.split(',',1)[1])))
        #stops.append((stop, walking_time(location,stop)))
    return stops
'''
    

    
#print(walking_time("MSC College Station", "Ross and Ireland - North, Ross Street & Ireland Street, College Station, TX 77840"))
#print(gmap.distance_matrix("MSC College Station", "Ross Street & Bizzell Street, College Station, TX 77840", mode='walking'))

#print(time_to_stops("MSC College Station"))

def next_bus_stop(bus_stop, route):
    next_stop = route[(route.index(bus_stop)+1) % len(route)]
    return ([(next_stop, driving_time(bus_stop.split(',',1)[1],next_stop.split(',',1)[1]))])


def route_time(stop1, stop2,start,end,route):
    i=route.index(stop1)
    total_time=0
    
    while(route[i]!=stop2):
        total_time+=driving_time(route[i],route[(i+1)%len(route)])
        i=(i+1)%len(route)
    return total_time + walking_time(start,stop1) + walking_time(stop2, end)

#(route_time("MSC - ILCB, 215 Lamar St, College Station, TX 77844", "Ross and Bizzell (South), Ross Street & Bizzell Street, College Station, TX 77840", "Rudder Tower, 401 Joe Routt Blvd, College Station, TX 77840", "Zachry Engineering Center, 125 Spence St, College Station, TX", Route1))
#print(route_time("Fish Pond, 233 Houston St, College Station, TX 77840", "Ross and Bizzell (South), Ross Street & Bizzell Street, College Station, TX 77840", "Rudder Tower, 401 Joe Routt Blvd, College Station, TX 77840", "Zachry Engineering Center, 125 Spence Street, College Station, TX", Route1))   

def return_key(route):
    for i in range(0,len(Routes)):
        if(Routes[list(Routes)[i]]==route):
            return list(Routes)[i]

def find_route(start_location,end_location, route):
    closest_starting_stops = closest_stop(start_location,route)
    closest_ending_stops = closest_stop(end_location,route)
    
    best_time = 10**99
    best_route = []
    
    for start_stop in closest_starting_stops:
        for end_stop in closest_ending_stops:
            current_time = route_time(start_stop, end_stop, start_location, end_location, route)
            if(current_time<best_time):
                best_time = current_time
                best_route = [(start_stop, end_stop)]
            elif(current_time == best_time):
                best_route.append((start_stop,end_stop))
    return (best_route, best_time, return_key(route))

#print(find_route("School of Public Health, 212 Adriance Lab Rd, College Station, TX 77843","NCTM, 100 Discovery Dr, College Station, TX 77845", Route8))


def find_best_route(start_location, end_location):
    best_time = 10**99
    best_route = []
    for route in list(Routes):
        path = find_route(start_location, end_location,Routes[route])
        if(path[1]<best_time):
            best_time=path[1]
            best_route = [path]
        elif(path[1]==best_time):
            best_route.append(path)
    return (best_route, best_time) 


def format_result(hello):
    answer=''
    answer += "Take " + hello[0][0][2][:-1] + " " + hello[0][0][2][-1] + "\n"
    answer += "Get on at " + hello[0][0][0][0][0] + "\n"
    answer += "Get off at " + hello[0][0][0][0][1] + "\n"
    answer += "Approximately " + str(hello[0][0][1]) + " minutes plus wait time"
    return answer
    
            
#print(find_best_route("School of Public Health, 212 Adriance Lab Rd, College Station, TX 77843","NCTM, 100 Discovery Dr, College Station, TX 77845"))
#print(format_result(find_best_route("hi,174-262 Adriance Lab Rd, College Station, TX 77845","Lot 44, 1000 MSRB Dr College Station, TX 77845")))  
print(format_result(find_best_route("Reed Arena/Lot 97, 730 Olsen Blvd, College Station, TX 77843", "Ag Building, Ag Building - Bus Stop 524, College Station, TX"))) 
print(format_result(find_best_route("hi,174-262 Adriance Lab Rd, College Station, TX 77845","Lot 44, 1000 MSRB Dr College Station, TX 77845")))     
  
            
#print(find_best_route("Rudder Tower, 401 Joe Routt Blvd, College Station, TX 77843","Zachary, 125 Spence St, College Station, TX 77840"))
#print(find_best_route("Reed Arena/Lot 97, 730 Olsen Blvd, College Station, TX 77843", "Ag Building, Ag Building - Bus Stop 524, College Station, TX"))

#print(driving_time("Reed Arena/Lot 97, 730 Olsen Blvd, College Station, TX 77843", "Ag Building, Bus Stop 524, College Station, TX"))
#print(closest_stop("School of Public Health, 212 Adriance Lab Rd, College Station, TX 77843", Route3))
#print(closest_stop("School of Public Health, 212 Adriance Lab Rd, College Station, TX 77843"))
#print(find_best_route("School of Public Health, 212 Adriance Lab Rd, College Station, TX 77843","NCTM, 100 Discovery Dr, College Station, TX 77845"))
'''
print(find_route("MSC, 275 Joe Routt Blvd, College Station, TX 77840","Zachary, 125 Spence St, College Station, TX 77840", Route3))
print(find_route("MSC, 275 Joe Routt Blvd, College Station, TX 77840","Zachary, 125 Spence St, College Station, TX 77840", Route4))
print(find_route("MSC, 275 Joe Routt Blvd, College Station, TX 77840","Zachary, 125 Spence St, College Station, TX 77840", Route5))
print(find_route("MSC, 275 Joe Routt Blvd, College Station, TX 77840","Zachary, 125 Spence St, College Station, TX 77840", Route6))
print(find_route("MSC, 275 Joe Routt Blvd, College Station, TX 77840","Zachary, 125 Spence St, College Station, TX 77840", Route8))'''
    
        
                      

        


    

#print(bus_stop_to_end(end_location))

#print(next_bus_stop("Commons, 676 Lubbock St, College Station, TX 77840", Route1))


'''
for stop in Route1:
    print(stop)
    print(end_location)
    print(gmap.distance_matrix(stop.split(',',1)[1], end_location.split(',',1)[1], mode='walking'))
    print(stop.split(',',1)[1])
    paths[stop]=time_to_stops(stop) + next_bus_stop(stop,Route1) + [(end_location, walking_time(stop.split(',',1)[1], end_location.split(',',1)[1]))]       


for route in Routes:
    for stop in route:
        paths[stop]=time_to_stops(stop) + next_bus_stop(stop,route) + [(end_location, walking_time(stop.split(',',1)[1], end_location.split(',',1)[1]))]

#print(paths["Commons, 676 Lubbock St, College Station, TX 77840"])
        
for route in Routes:
    for stop in route:
        paths[start_location]= time_to_stops(start_location)
        
'''
        
        
#print(paths)'''
        


    

'''#print(closest_stops("MSC College Station"))


#print(next_bus_stop(Route1[0], Route1))
#print(closest_stop("MSC College Station", Route1))
#print(walking_time("MSC College Station", "MSC College Station"))
#print(closest_stops(Route1[0]))'''


'''for route in Routes:
    for stop in route:
        paths[stop]= next_bus_stop(stop,route) + closest_stops(stop)'''
       
        

'''for Route in Routes:
    for Stop in Route:'''
                                             
                        
            
        
        
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