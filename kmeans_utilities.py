
import numpy as np
import matplotlib.pyplot as plt

def euclidean_distance(a,b):
    """
    Assuming that a and b are each tuples representing points, 
    calculate the euclidean distance beween them.
    """
    return np.linalg.norm(np.array(a) - np.array(b))

def average_point(points):
    """
    Take in a list of points, where each point is a tuple.
    Return the average of the points.
    """
    return tuple(np.mean(np.array(points), axis=0))

def points_equal(centroids1, centroids2):
    """
    Given two lists of points, check that they are equal.
    Allow a floating-point error of epsilon along each dimension.
    """
    epsilon = 0.001
    return np.all(np.array(centroids1) - np.array(centroids2) < epsilon)

# In this version, return the point as a numpy array
def average_point_array(points):
    """
    Take in a list of points, where each point is a tuple.
    Return the average of the points.
    """
    return np.mean(np.array(points), axis=0)

# A plotting function so we can visualise results
# This function plots data assuming points are a list of tuples
def plot_kmeans(data, centroids, assignments, k):
    for cluster in range(k):
        cluster_points = [p for (p,assignment) in zip(data,assignments) 
                            if assignment==cluster]
        x_values = [x for (x,y) in cluster_points]
        y_values = [y for (x,y) in cluster_points]
        plt.scatter(x_values,y_values)
    centroid_x_values = [x for (x,y) in centroids]
    centroid_y_values = [y for (x,y) in centroids]
    plt.scatter(centroid_x_values,centroid_y_values,marker='x',s=80,c='k')
    plt.show()


'''
# For the curious, versions of functions with no numpy arrays or vector maths

def points_equal(centroids1, centroids2):
    for (c1,c2) in zip(centroids1, centroids2):
        # Check that this old and new pair of centroids are the same along every dimension
        for (v1,v2) in zip(c1,c2):
            if np.abs(v1-v2) >= epsilon:
                return False
    return True

def average_point(centroid_points):
    """
    Take in a list of points, where each point is a tuple.
    Return the average of the points.
    """
    centroid = []
    for dimension_values in zip(*centroid_points):
        centroid.append(np.mean(dimension_values))
    return tuple(centroid)
'''