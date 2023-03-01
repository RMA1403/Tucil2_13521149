from typing import List, Tuple
from random import uniform

def euclidean_distance(point_1: List[float], point_2: List[float]) -> float:
  """Calculate the euclidean distance between two points
  
  Paramters
  ---------
  point_1 : First point
  point_2 : Second point

  Returns
  -------
  Euclidean distance between the first and second point
  """
  sum = 0
  for i in range(len(point_1)):
    sum += (point_1[i]-point_2[i])**2

  return sum**(1/2)

def min3(f1: float, f2: float, f3: float) -> Tuple[float, int, int]:
  """Find the minimum of three values
  
  Parameters
  ----------
  f1 : First value
  f2 : Second value
  f3 : Third value

  Returns
  -------
  Minimum of the three values
  """
  if f1 <= f2 and f1 <= f3 :
    return f1, 0, 1
  elif f2 <= f1 and f2 <= f3 :
    return f2, 0, 2
  else:
    return f3, 1, 2

def get_random_points(num_points: int, dimension: int) -> List[List[float]]:
  """Generate a random list of points in a range from -500 to 500
  
  Parameters
  ----------
  num_points : Number of points
  dimension : Dimension of each points

  Returns
  -------
  List of points
  """
  return [[uniform(-500, 500) for _ in range(dimension)] for _ in range(num_points)]