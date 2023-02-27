from typing import List, Tuple

from functions.utility import euclidean_distance, min3

def is_in_strip(p1: List[float], p2: List[float], d: float) -> bool:
  for i in range(len(p1)):
    if abs(p1[i] - p2[i] > d):
      return False
  return True

def closest_pair_strip(left: List[List[float]], right: List[List[float]], d: float, p1: List[float], p2: List[float]) -> float:
  min_d = d
  min_p1 = p1
  min_p2 = p2
  for p1 in left:
    for p2 in right:
      if is_in_strip(p1, p2, d):
        temp_d = euclidean_distance(p1, p2)
        if temp_d < min_d:
          min_d = temp_d
          min_p1 = p1
          min_p2 = p2
  return min_d, min_p1, min_p2

def closest_pair(points: List[List[float]]) -> Tuple[float, List[float], List[float]]:
  if len(points) == 2:
    return euclidean_distance(points[0], points[1]), points[0], points[1]
  elif len(points) == 3:
    min_d, i1, i2 = min3(euclidean_distance(points[0], points[1]), 
                      euclidean_distance(points[0], points[2]), 
                      euclidean_distance(points[1], points[2]))
    return(min_d, points[i1], points[i2])
  else:
    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]

    d1, l1, l2 = closest_pair(left)
    d2, r1, r2 = closest_pair(right)
    min_d, min_p1, min_p2 = (d1, l1, l2) if d1 <= d2 else (d2, r1, r2)

    d3, s1, s2 = closest_pair_strip(left, right, min_d, min_p1, min_p2)
    min_d, min_p1, min_p2 = (d3, s1, s2) if d3 <= min_d else (min_d, min_p1, min_p2)

    return min_d, min_p1, min_p2    