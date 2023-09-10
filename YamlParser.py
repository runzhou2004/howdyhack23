import yaml
import googlemaps

with open("routes.yaml", "r") as stream:
    try:
        data = (yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)
        
for addy in data['12th man']:
    addy = addy.split(',')
    print(f'{addy[0]} {addy[1]}')