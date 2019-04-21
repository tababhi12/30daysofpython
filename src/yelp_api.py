import requests
import json
api_key = 'QckQ4YpbZ819kvujGxxBHwU3Uc4_z99l9JoP8PJY287cboAvrMsptlsiEaN0jhRsOf71xF2Bgq1pHlOJWboOZJqEfA5TNycA9xMNkTrCXZ1hBYgn4NOdwvlzRlO8XHYx'
headers = {'Authorization':'Bearer %s' %api_key}

url = 'https://api.yelp.com/v3/businesses/search'
param = {'term':'seafood','location':'New York City'}

req = requests.get(url,params = param,headers= headers)
print(req.status_code)
response = req.json()
for i in response['businesses']:
    print(i["name"])
    print(i["phone"])
    print(i["location"]["display_address"])
    print(i["location"]["city"])