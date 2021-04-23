from yaml import load, FullLoader
from miniupnpc import UPnP


# load the configuration file
with open('config.yaml') as f:
    config = load(f, Loader=FullLoader)

# use UPnP to get the external IP address
upnp = UPnP()

upnp.discoverdelay = 200
upnp.discover()
upnp.selectigd()
ip = upnp.externalipaddress()

