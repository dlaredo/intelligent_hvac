import zeep
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session as WebSession
from datetime import datetime, timezone, timedelta


def getClient(servicewsdl):
	"""Attempt to stablish a connection to the webservice and return a client object connected to servicewsdl webservice"""

	client = None

	try:
		webSession = WebSession()
		webSession.auth = HTTPBasicAuth('soap', "")
		transport = Transport(timeout=10, session = webSession)
		client = zeep.Client(wsdl=servicewsdl, transport=transport)
		print('Client successfully created')
	except Exception as e:
		print("Error in getting a client to the webservice")

	return client


def main():

	Trendwsdl = 'http://10.20.0.47/_common/webservices/TrendService?wsdl'

	trendServiceClient = getClient(Trendwsdl)

	PDT = timezone(-timedelta(hours=7), 'PDT')

	path = '#ahu-4_0206/rf3_vel_press'

	#startDateTime = datetime(2017, 2, 1, hour=0, minute=0, second=0, microsecond=0, tzinfo=PDT)
	#endDateTime = datetime(2017, 2, 1, hour=0, minute=0, second=0, microsecond=0, tzinfo=PDT)

	startDateTime = datetime(2016, 8, 9, hour=13, minute=55, second=0, microsecond=0, tzinfo=PDT)
	endDateTime = datetime(2016, 8, 9, hour=14, minute=0, second=0, microsecond=0, tzinfo=PDT)


	data = trendServiceClient.service.getTrendData('soap',"", path, startDateTime.strftime("%m/%d/20%y %I:%M:%S %p"), endDateTime.strftime("%m/%d/20%y %I:%M:%S %p"), False, 0)
	print(path, data)

main()