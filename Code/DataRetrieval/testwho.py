import BAC0
import logging

logger = logging.getLogger('BAC0')
logger.setLevel('DEBUG')
handler = logging.FileHandler('BAC0Log.txt', mode='a')
handler.setLevel('DEBUG')
logger.addHandler(handler)

bacnet = BAC0.connect('127.0.0.1', bokeh_server=False)

bacnet.whois()
print(bacnet.devices)