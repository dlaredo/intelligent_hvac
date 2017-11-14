import matplotlib.pyplot as plt
import matplotlib.font_manager
import seaborn as sns
import random


def jp_plotData(dataFrame, titleString, saveToFile='', nsamples = 100, vars=None, hue=None):
	"""Generate plots of the data in dataframe. Right now only joinplots are generated"""

	#plot nsamples random elements from the sample
	random_elements = random.sample(range(dataFrame.shape[0]), nsamples)
	dataFrame_plot = dataFrame.iloc[random_elements]

	print(dataFrame_plot.shape)

	if vars != None:
		p = sns.pairplot(dataFrame_plot, hue=hue, diag_kind='kde', vars=vars, dropna=True)
	else:
		p = sns.pairplot(dataFrame_plot, hue=hue, diag_kind='kde', dropna=True)

	plt.suptitle(titleString, y = 1.025)

	if saveToFile != '':
		plt.savefig(saveToFile, format='png', pad_inches=0.5, bbox_inches='tight')
		plt.close()
	else:
		pass
		#plt.show()