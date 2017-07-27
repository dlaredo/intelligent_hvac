import anomaly_detection
from datetime import datetime


def main():
	"""Main function"""

	desiredComponents = ['Thermafuser']

	startDateTime = datetime(2017, 1, 1, hour=0, minute=0, second=0, microsecond=0)
	endDateTime = datetime(2017, 1, 1, hour=0, minute=10, second=0, microsecond=0)

	dataFrames = anomaly_detection.loadData(startDateTime, endDateTime, desiredComponents)
	print("DataFrames created")

	#clean dataframe and reshape it
	for dfkey in dataFrames:
    newColumnNames = {column:column.replace('_', "") for column in dataFrames[dfkey].columns}
    
    #Get the Id Column
    idColumn = list(filter(lambda colName: 'Id' in colName, newColumnNames.values()))
    if len(idColumn) != 1:
        print('Could not determine Id Column')
    else:
        idColumn = idColumn[0]
        print(idColumn)
    
    dataFrames[dfkey].rename(columns=newColumnNames, inplace=True)
    dataFrames[dfkey].set_index(['timestamp', idColumn], inplace=True)
    dataFrames[dfkey].dropna(axis=1, how='all', inplace=True)
    #dataFrames[dfkey].fillna(value=nan, inplace=True)

main()