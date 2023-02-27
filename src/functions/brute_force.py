from errno import EWOULDBLOCK
from typing import List, Tuple

from functions.utility import euclidean_distance

def brute_force(points: List[List[float]]) -> Tuple[float, List[float], List[float]]:
  min_distance, point_1, point_2 = euclidean_distance(points[0], points[1]), points[0], points[1]
  
  for i in range(len(points)):
    for j in range(len(points)):
      temp_min = euclidean_distance(points[i], points[j])
      if i != j and temp_min < min_distance:
        min_distance, point_1, point_2 = temp_min, points[i], points[j]

  return min_distance, point_1, point_2