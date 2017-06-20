import pandas as pd
import tkinter as tk
import numpy as np
import matplotlib
import matplotlib.cm as cmx
import matplotlib.colors as colors
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from tkinter import filedialog
from sklearn import preprocessing
from sklearn import cluster
from sklearn import manifold
from mpl_toolkits.mplot3d import Axes3D

def read_pandas_csv(filename):
	"""Read the contents of a csv file using pandas framework"""

	df = pd.read_csv(filename)

	#drop the temperature header, since it is the index pandas will use for the dataframe.
	new_headers = df.columns.values.tolist()
	new_headers = new_headers[1:]

	#create the new dataframe with the appropriate headers
	df = df.drop(new_headers[len(new_headers) - 1], axis=1)

	#Replace the old headers by the new headers
	new_headers[0] = new_headers[0].replace("[", "")
	new_headers[len(new_headers) - 1] = new_headers[len(new_headers) - 1].replace("]", "")

	for i in range(len(new_headers)):
		new_headers[i] = new_headers[i].replace("'", "")

	df.columns = new_headers

	return df

def create_dataframe_from_files(file_paths):
	"""From the files file_list create a dataframe containing the data corresponding to the summary of the files"""

	df_cols = list()

	#create the structure of the dataframe
	df_temp = read_pandas_csv(file_paths[0])
	print(df_temp)
	summary_stats = df_temp.describe()
	column_names = df_temp.columns.values
	temp_stats = summary_stats[column_names[0]]
	describe_items = temp_stats.index

	for column in column_names:
		for item in describe_items:
			df_cols.append(column.replace(" ", "") + '_' + item)

	#Create dictionary to add all of the rows for the dataframe. This is more efficient than adding rows to the dataframe.
	d = {}

	for file_path in file_paths:
		df_temp = read_pandas_csv(file_path)
		date = df_temp.index.values[0].split()[0]
		summary_stats = df_temp.describe()

		col = list()

		for column in df_temp.columns:
			summary_stats_values = summary_stats[column].values
			col.extend(summary_stats_values)
		
		d[date] = pd.Series(col, index = df_cols)

	#Create the dataframe from the dictionary previously created
	df = pd.DataFrame(d)

	return df

def get_spaced_colors(n):
    max_value = 16581375 #255**3
    interval = int(max_value / n)
    colors_array = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]
    
    return [(int(i[:2], 16)/255, int(i[2:4], 16)/255, int(i[4:], 16)/255) for i in colors_array]


def main():

	#Create dialog window to open the files to be analized
	root = tk.Tk()
	root.withdraw()

	options = {}
	options['filetypes'] = [('text files', '.csv')]
	options['multiple'] = True
	options['title'] = 'Select the files to analize'

	file_paths = filedialog.askopenfilenames(**options)

	df = create_dataframe_from_files(file_paths)

	#drop some colums from the dataframe
	index_drop_columns = list()
	for string in df.index:
		if string.find("count") != -1:
			index_drop_columns.append(string)

	df2 = df.drop(index_drop_columns).T
	print(df2)

	#Preprocess data (standardize it)
	df_transformed = preprocessing.scale(df2)

	#print(df_transformed)

	#Perform mean shift algorithm
	clf = cluster.MeanShift()
	clf.fit(df_transformed)

	print(clf.cluster_centers_)
	#print(clf.labels_)
	print("{} clusters found by meanshift".format(len(clf.cluster_centers_)))
	#print(len(clf.labels_))

	#Transform the data using MDS technique for its visualization
	#print("{} is the size of the dataframe".format(df_transformed.shape))
	#print(df_transformed)
	#print("{} is the size of the cluster centers".format(clf.cluster_centers_.shape))
	#print(clf.cluster_centers_)
	appended_array = np.append(df_transformed, clf.cluster_centers_, axis = 0)
	#print("{} is the size of the appended array".format(appended_array.shape))

	#Perform kmeans clustering
	kclf = cluster.KMeans(n_clusters = 2)
	kclf.fit(df_transformed)

	print("{} clusters found by kmeans".format(len(kclf.cluster_centers_)))
	appended_array2 = np.append(df_transformed, kclf.cluster_centers_, axis = 0)

	#Create color array
	#cmap = get_spaced_colors(len(clf.cluster_centers_) + 1)

	cmap = ['b', 'g', 'r', 'c', 'm', 'k']*10

	#Plot data for mean shift	
	n_labels = len(clf.labels_)

	mnf = manifold.MDS(3)
	mnf.fit(appended_array)
	mnf2 = manifold.MDS()
	mnf2.fit(appended_array)

	#generate color list for the clusters
	color_array  = list()
	for label in clf.labels_:
		color_array.append(cmap[label])

	#plot the data 2D
	fig = plt.figure()
	
	plt.scatter(mnf.embedding_[:n_labels,0], mnf.embedding_[:n_labels,1], c = color_array)
	plt.scatter(mnf.embedding_[n_labels:,0], mnf.embedding_[n_labels:,1], c = 'g', marker='x', s = 100)

	plt.xlabel('X Label')
	plt.ylabel('Y Label')
	plt.title('Mean shift 2D plot')

	#plot the data 3D
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	ax.scatter(mnf.embedding_[:n_labels,0], mnf.embedding_[:n_labels,1], mnf.embedding_[:n_labels,2], c = color_array)
	ax.scatter(mnf.embedding_[n_labels:,0], mnf.embedding_[n_labels:,1], mnf.embedding_[n_labels:,2], c = 'g', marker='x', s = 100)

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.title('Mean shift 3D plot')

	#Plot data for kmeans	
	n_labels = len(kclf.labels_)

	mnf = manifold.MDS(3)
	mnf.fit(appended_array2)
	mnf2 = manifold.MDS()
	mnf2.fit(appended_array2)

	#generate color list for the clusters
	color_array  = list()
	for label in kclf.labels_:
		color_array.append(cmap[label])

	#plot the data 2D
	fig = plt.figure()
	
	plt.scatter(mnf.embedding_[:n_labels,0], mnf.embedding_[:n_labels,1], c = color_array)
	plt.scatter(mnf.embedding_[n_labels:,0], mnf.embedding_[n_labels:,1], c = 'g', marker='x', s=100)

	plt.xlabel('X Label')
	plt.ylabel('Y Label')
	plt.title('KMeans 2D plot')

	#plot the data 3D
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	ax.scatter(mnf.embedding_[:n_labels,0], mnf.embedding_[:n_labels,1], mnf.embedding_[:n_labels,2], c = color_array)
	ax.scatter(mnf.embedding_[n_labels:,0], mnf.embedding_[n_labels:,1], mnf.embedding_[n_labels:,2], c = 'g', marker='x', s=100)

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.title('KMeans 3D plot')

	plt.show()


if __name__ == '__main__':
    main()