from miniupnpc import UPnP


upnp = UPnP()

upnp.discover()
upnp.selectigd()
ip = upnp.externalipaddress()

