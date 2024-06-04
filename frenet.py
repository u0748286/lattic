import numpy as np

def calculate_frenet_coordinates(curve_points, point_p):
    """
    Calculate the Frenet coordinates for a point with respect to a given curve.
    
    Parameters:
    curve_points (numpy.ndarray): An array of points defining the curve.
    point_p (numpy.ndarray): The point for which to find the Frenet coordinates.
    
    Returns:
    s (float): The arc length from the curve's start to the projection of point_p onto the curve.
    d (float): The lateral offset from the curve to point_p.
    """
    
    # Calculate the distance from point_p to each point on the curve
    distances = np.linalg.norm(curve_points - point_p, axis=1)

    # Find the closest point on the curve to point_p
    closest_point_index = np.argmin(distances)
    closest_point = curve_points[closest_point_index]

    # Calculate the arc length 's' from the start of the curve to the closest point
    if closest_point_index > 0:
        s = np.sum(np.linalg.norm(np.diff(curve_points[:closest_point_index+1], axis=0), axis=1))
    else:
        s = 0

    # Calculate the lateral offset 'd' from the closest point on the curve to point_p
    tangent_vector = curve_points[1] - curve_points[0] if closest_point_index == 0 else curve_points[closest_point_index] - curve_points[closest_point_index - 1]
    tangent_vector /= np.linalg.norm(tangent_vector)
    normal_vector = np.array([-tangent_vector[1], tangent_vector[0]])
    p_to_closest_vector = point_p - closest_point
    d = np.dot(p_to_closest_vector, normal_vector)
    
    return s, d

# Example usage:
# Define the curve as a numpy array of points
curve_points = np.array([[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]])
# Define the point for which to calculate Frenet coordinates
point_p = np.array([3, 2])
# Calculate Frenet coordinates
s, d = calculate_frenet_coordinates(curve_points, point_p)
print("Frenet coordinates (s, d):", s, d)
