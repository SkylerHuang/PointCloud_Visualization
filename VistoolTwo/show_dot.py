import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visual_pointcloud(point_cloud,save=False):
    if (point_cloud.shape[0]) == 0:
        return None

    fig=plt.figure('point cloud')
    ax=fig.add_subplot(111,projection='3d')

    plt.axis('off')
    ax.set_xbound(-1,1)
    ax.set_ybound(-1,1)
    ax.set_zbound(-1,1)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.scatter(point_cloud[:, 0], point_cloud[:, 1], point_cloud[:, 2], marker='o', s=1.5, linewidth=0, alpha=1,
               cmap='Spectral')

    if save == True:
        plt.savefig('visualize.jpg')
    else:
        plt.show()