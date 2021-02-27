import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas

base_dir = "/Users/simone/CLionProjects/Midterm_Parallel_Computing_K-means/output/"


def plot_k_means_iteration(k, iteration=2147483647):
    df_dataset = pandas.read_csv(base_dir + 'k' + str(k) + 'iteration' + str(iteration) + '.csv', header=None)
    df_centroids = pandas.read_csv(base_dir + 'k' + str(k) + 'centroids' + str(iteration) + '.csv', header=None)

    cluster = []
    for i in range(k):
        cluster.append(df_dataset.loc[df_dataset[3] == i])

    fig = plt.figure()

    for i in range(k):
        plt.scatter(cluster[i].iloc[:, 0], cluster[i].iloc[:, 1])

    plt.scatter(df_centroids.iloc[:, 0], df_centroids.iloc[:, 1], marker='*', c='black')

    plt.show()

plot_k_means_iteration(10)
