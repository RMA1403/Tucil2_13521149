import matplotlib.pyplot as plt

def visualize(_points, point_1, point_2):
  """Visualize closest-pair of point in three dimension
  
  Parameters
  ----------
  _points : List of points
  point_1 : First point forming the closest-pair
  point_2 : Second point forming the closest-pari

  Returns
  -------
  """
  points = _points[:]
  fig = plt.figure()

  axis = fig.add_subplot(111, projection='3d')
  for i in range(len(points)):
    axis.scatter(points[i][0], points[i][1], points[i][2], c='b', marker='o')

  axis.scatter(point_1[0], point_1[1], point_1[2], c='r', marker='o')
  axis.scatter(point_2[0], point_2[1], point_2[2], c='r', marker='o')

  axis.set_xlim([-500, 500])
  axis.set_ylim([-500, 500])
  axis.set_zlim([-500, 500])

  axis.set_xlabel('X')
  axis.set_ylabel('Y')
  axis.set_zlabel('z')

  plt.show()

  