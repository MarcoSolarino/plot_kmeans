import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas

base_dir = "/Users/simone/CLionProjects/Midterm_Parallel_Computing_K-means/output/"


def plot_k_means_iteration(k, iteration):
    df_dataset = pandas.read_csv(base_dir + 'k' + str(k) + 'iteration' + str(iteration) + '.csv', header=None)
    df_centroids = pandas.read_csv(base_dir + 'k' + str(k) + 'centroids' + str(iteration) + '.csv', header=None)

    data0 = df_dataset.loc[df_dataset[3] == 0]
    data1 = df_dataset.loc[df_dataset[3] == 1]
    data2 = df_dataset.loc[df_dataset[3] == 2]

    fig = plt.figure()

    plt.scatter(data0.iloc[:, 0], data0.iloc[:, 1])
    plt.scatter(data1.iloc[:, 0], data1.iloc[:, 1])
    plt.scatter(data2.iloc[:, 0], data2.iloc[:, 1])
    plt.scatter(df_centroids.iloc[:, 0], df_centroids.iloc[:, 1], marker='*', c='black')

    plt.show()

    return df_dataset


plot_k_means_iteration(5, 1)