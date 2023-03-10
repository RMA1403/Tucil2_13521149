from errno import EWOULDBLOCK
from typing import List, Tuple

from functions.utility import euclidean_distance

def brute_force(points: List[List[float]]) -> Tuple[float, List[float], List[float], int]:
  """Brute force algorithm for finding closest-pair of points

  Parameters
  ----------
  points : List of points

  Returns
  -------
  Tuple containing the shortest distance, two points forming the closest-pair, and the number
  of euclidian distance operation performed
  """
  count_euc = 0
  min_distance, point_1, point_2 = euclidean_distance(points[0], points[1]), points[0], points[1]

  # Checks for every possible pair of points
  for i in range(len(points)):
    for j in range(len(points)):
      temp_min = euclidean_distance(points[i], points[j])
      count_euc += 1

      if i != j and temp_min < min_distance:
        min_distance, point_1, point_2 = temp_min, points[i], points[j]

  return min_distance, point_1, point_2, count_euc