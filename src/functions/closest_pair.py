from typing import List

from functions.utility import euclidean_distance, min3

def is_in_strip(p1: List[float], p2: List[float], d: float) -> bool:
  for i in range(len(p1)):
    if abs(p1[i] - p2[i] > d):
      return False
  return True

def closest_pair_strip(left: List[List[float]], right: List[List[float]], d: float) -> float:
  min_d = d
  for p1 in left:
    for p2 in right:
      if is_in_strip(p1, p2, d):
        temp_d = euclidean_distance(p1, p2)
        if temp_d < min_d:
          min_d = temp_d
  return min_d


def closest_pair(points: List[List[float]]) -> float:
  if len(points) == 2:
    return euclidean_distance(points[0], points[1])
  elif len(points) == 3:
    return min3(euclidean_distance(points[0], points[1]), 
                euclidean_distance(points[0], points[2]), 
                euclidean_distance(points[1], points[2]))
  else:
    mid = len(points)//2
    left = points[:mid+1]
    right = points[mid+1:]

    d1 = closest_pair(left)
    d2 = closest_pair(right)
    min_d = d1 if d1 <= d2 else d2

    d3 = closest_pair_strip(left, right, min_d)
    min_d = d3 if d3 <= min_d else min_d

    return min_d