import zeep
import traceback
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session
from datetime import datetime, timezone, timedelta

Evalwsdl = 'http://10.20.0.47/_common/webservices/Eval?wsdl'
Trendwsdl = 'http://10.20.0.47/_common/webservices/TrendService?wsdl'

#datetime object that uses the local PST time
startTime = datetime(2017, 6, 21, 15, 0, 0, 0, timezone(-timedelta(hours=8)))
endTime = datetime(2017, 6, 21, 15, 5, 0, 0, timezone(-timedelta(hours=8)))

try:
	session = Session()
	session.auth = HTTPBasicAuth('soap', "")
	transport = Transport(timeout=30, session = session)
	#client = zeep.Client(wsdl=wsdl, transport=transport)
	client = zeep.Client(wsdl=Trendwsdl, transport=transport)
	path = '#1c1a_thermafuser/m073'
	#value = client.service.getValue('#1c1a_thermafuser/air_flow_fdbk')
	print(endTime.strftime("%m/%d/20%y %I:%M:%S %p"))
	data = client.service.getTrendData('soap',"", path, startTime.strftime("%m/%d/20%y %I:%M:%S %p"), endTime.strftime("%m/%d/20%y %I:%M:%S %p"), False, 0)
	print(data)
except Exception as e:
		print(traceback.format.exc())
		print("error")