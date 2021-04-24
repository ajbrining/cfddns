from yaml import load, FullLoader
from miniupnpc import UPnP
import requests

# load the configuration file
with open('config.yaml') as f:
    config = load(f, Loader=FullLoader)

# use UPnP to get the external IP address
upnp = UPnP()

upnp.discoverdelay = 200
upnp.discover()
upnp.selectigd()
ip = upnp.externalipaddress()

# set up variables needed for api access
api_url = 'https://api.cloudflare.com/client/v4'
headers = {'Authorization': 'Bearer ' + config['api_token'],
           'Content-Type': 'application/json'}

# get the DNS record so we can save the ID and check the IP
url = '{}/zones/{}/dns_records?name={}'.format(api_url, config['zone_id'], config['hostname'])
response = requests.get(url, headers=headers).json()

if response['result'][0]['content'] == ip:
    exit

# update the DNS record with cloudflare
url = '{}/zones/{}/dns_records/{}'.format(api_url, config['zone_id'], response['result'][0]['id'])
data = '{{"content": "{}"}}'.format(ip)
requests.patch(url, headers=headers, data=data)
