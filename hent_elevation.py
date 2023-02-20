# https://requests.readthedocs.io/en/latest/user/quickstart/
# skal installeres ved at skrive denne kommando i cmd/powershell `pip install requests`
import requests

# Adresse data

# https://dataforsyningen.dk/data/4729

api_url = 'https://api.dataforsyningen.dk/'
endpoint = 'adresser'

params = {
    'vejnavn'       : 'Telegrafvej',
    'husnr'         : '9',
    'postnrnavn'    :  'Ballerup',
    'struktur'      : 'mini',
    }

respons = requests.get(api_url+endpoint, params)

print(respons)
print("Response status:", respons.status_code)

if respons.status_code == 200:
    print(respons.json())
    rjson = respons.json()[0]
    print("Latitude (bredde):", rjson['x'])
    print("Longitude (længde):", rjson['y'])

# curl https://api.opentopodata.org/v1/eudem25m?locations=57.688709,11.976404

elev_api_url = "https://api.opentopodata.org/"
elev_endpoint = "v1/eudem25m"

params = {
    #'locations' : '[(' + str(rjson['y']) + ',' + str(rjson['x']) + '),' + '(55.73145776633826,12.35328065110478)]',
    'locations' : str(rjson['y']) + ',' + str(rjson['x'])
}

print(params)

respons = requests.get(elev_api_url+elev_endpoint, params)

print(respons)
print("Response status:", respons.status_code)

if respons.status_code == 200:
    print(respons.json())
    print('elevation:', respons.json()['results'][0]['elevation'])