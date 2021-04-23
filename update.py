from yaml import load, FullLoader
from miniupnpc import UPnP


# load the configuration file
with open('config.yaml') as f:
    config = load(f, Loader=FullLoader)

upnp = UPnP()

upnp.discover()
upnp.selectigd()
ip = upnp.externalipaddress()

