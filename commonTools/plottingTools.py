import matplotlib.pyplot as plt
import matplotlib.font_manager
import seaborn as sns


def plotData(dataFrame, titleString, saveToFile=False, nsamples = 100, vars=None):
	"""Generate plots of the data in dataframe. Right now only joinplots are generated"""

	#plot nsamples random elements from the sample
	random_elements = random.sample(range(dataFrame.shape[0]), nsamples)
	dataFrame_plot = dataFrame.iloc[random_elements]

	if vars != None:
		p = sns.pairplot(dataFrame_plot, hue='AHUNumber', diag_kind='kde', vars=vars, dropna=True)
	else:
		p = sns.pairplot(dataFrame_plot, hue='AHUNumber', diag_kind='kde', dropna=True)

	plt.suptitle(titleString, y = 1.025)

	if saveToFile == True:
		plt.savefig('testfig.png', format='png', pad_inches=0.5, bbox_inches='tight')
		plt.close()
	else:
		pass
		#plt.show()