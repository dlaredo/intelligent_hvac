import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.font_manager
import seaborn as sns
import pandas as pd
from datetime import datetime
from sklearn.covariance import EllipticEnvelope
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
from dataManagement import DataManager


def main():

	dataManager = DataManager(user="", password="", engineType="", dbName="", host="", port="")

	classifiers = {'EllipticEnvelope':EllipticEnvelope(contamination=0.035)}

	pd.options.mode.chained_assignment = None

	nsamples = 1000

	desiredComponents = ['Valve']

	startDateTime = datetime(2017, 11, 6, hour=0, minute=0, second=0, microsecond=0)
	endDateTime = datetime(2017, 3, 1, hour=0, minute=0, second=0, microsecond=0)

	dataFrames = getDesiredData(desiredComponents, startDateTime, endDateTime, removeSetpoints=True, removeRequests=True, removeBooleans=True)