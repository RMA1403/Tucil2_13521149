from ctypes import pointer
from typing import List, Tuple

from functions.utility import euclidean_distance, min3

def is_in_strip(point_1: List[float], point_2: List[float], width: float) -> bool:
  for i in range(len(point_1)):
    if abs(point_1[i] - point_2[i] > width):
      return False
  return True

def closest_pair_strip(left: List[List[float]], right: List[List[float]], width: float, _point_1: List[float], _point_2: List[float]) -> Tuple[float, List[float], List[float]]:
  count_euc = 0
  min_distance, point_1, point_2 = width, _point_1, _point_2

  for point_left in left:
    for point_right in right:
      if is_in_strip(point_left, point_right, width):
        temp_distance = euclidean_distance(point_left, point_right)
        count_euc += 1

        if temp_distance < min_distance:
          min_distance, point_1, point_2 = temp_distance, point_left, point_right

  return min_distance, point_1, point_2, count_euc

def closest_pair(points: List[List[float]]) -> Tuple[float, List[float], List[float], int]:
  if len(points) == 2:
    return euclidean_distance(points[0], points[1]), points[0], points[1], 1
  elif len(points) == 3:
    min_distance, index_1, index_2 = min3(euclidean_distance(points[0], points[1]), 
                                          euclidean_distance(points[0], points[2]), 
                                          euclidean_distance(points[1], points[2]))
    return min_distance, points[index_1], points[index_2], 3
  else:
    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]

    min_left, point_left_1, point_left_2, count_left = closest_pair(left)
    min_right, point_right_1, point_right_2, count_right = closest_pair(right)

    min_distance, point_1, point_2 = (min_left, point_left_1, point_left_2) if min_left <= min_right else (min_right, point_right_1, point_right_2)

    min_strip, point_strip_1, point_strip_2, count_strip = closest_pair_strip(left, right, min_distance, point_1, point_2)

    min_distance, point_1, point_2 = (min_strip, point_strip_1, point_strip_2) if min_strip <= min_distance else (min_distance, point_1, point_2)

    count_euc = count_left + count_right + count_strip
    return min_distance, point_1, point_2, count_euc