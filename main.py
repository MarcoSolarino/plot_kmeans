import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas


def plot_k_means_iteration(dataset, centroids):
    df_dataset = pandas.read_csv(dataset, header=None)
    df_centroids = pandas.read_csv(centroids, header=None)

    data0 = df_dataset.loc[df_dataset[3] == 0]
    data1 = df_dataset.loc[df_dataset[3] == 1]
    data2 = df_dataset.loc[df_dataset[3] == 2]

    fig = plt.figure()

    # 3d case
    # ax = fig.add_subplot(111, projection='3d')
    #
    # ax.scatter(data0.iloc[:, 0], data0.iloc[:, 1], data0.iloc[:, 2], c='red')
    # ax.scatter(df_centroids.iloc[:, 0], df_centroids.iloc[:, 1], df_centroids.iloc[:, 2], marker='*', c='black')
    # ax.scatter(data1.iloc[:, 0], data1.iloc[:, 1], data1.iloc[:, 2], c='green')
    # ax.scatter(data2.iloc[:, 0], data2.iloc[:, 1], data2.iloc[:, 2], c='blue')
    #
    # ax.set_xlabel('X Axis')
    # ax.set_ylabel('Y Axis')
    # ax.set_zlabel('Z Axis')

    # 2d case
    plt.scatter(data0.iloc[:, 0], data0.iloc[:, 1], c='red')
    plt.scatter(data1.iloc[:, 0], data1.iloc[:, 1], c='green')
    plt.scatter(data2.iloc[:, 0], data2.iloc[:, 1], c='blue')
    plt.scatter(df_centroids.iloc[:, 0], df_centroids.iloc[:, 1], marker='*', c='black')

    plt.show()

    return df_dataset


for i in range(3):
    plot_k_means_iteration("D:/JetBrains/Projects/Clion/Kmeans/output/iteration" + str(i) + ".csv", "D:/JetBrains/Projects/Clion/Kmeans/output/centroids" + str(i) + ".csv")

