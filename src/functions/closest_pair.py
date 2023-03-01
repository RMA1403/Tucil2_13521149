from typing import List, Tuple

from functions.utility import euclidean_distance, min3

def is_in_strip(point_1: List[float], point_2: List[float], width: float) -> bool:
  """Checks whether a pair of point is in a strip
  
  Parameters
  ----------
  point_1 : First point
  point_2 : Second point
  width : Width of the strip

  Returns
  -------
  True if both points is in the strip
  """
  for i in range(len(point_1)):
    if abs(point_1[i] - point_2[i] > width):
      return False

  return True

def closest_pair_strip(left: List[List[float]], right: List[List[float]], width: float, _point_1: List[float], _point_2: List[float]) -> Tuple[float, List[float], List[float], int]:
  """Find the closest-pair of points across two areas divided by a strip
  
  Parameters
  ----------
  left : First area of points
  right : Second area of points
  width : Width of the strip
  _point_1 : Dummy point to be returned if there are no points in the strip
  _point_2 : Dummy point to be returned if there are no points in the strip

  Returns
  -------
  Tuple containing the shortest distance, two points forming the closest-pair, and the number
  of euclidian distance operation performed
  """
  count_euc = 0
  min_distance, point_1, point_2 = width, _point_1, _point_2

  # Iterates every possible pair of points
  for point_left in left:
    for point_right in right:
      # Checks if both points are in the strip
      if is_in_strip(point_left, point_right, width):
        temp_distance = euclidean_distance(point_left, point_right)
        count_euc += 1

        if temp_distance < min_distance:
          min_distance, point_1, point_2 = temp_distance, point_left, point_right

  return min_distance, point_1, point_2, count_euc

def closest_pair(points: List[List[float]]) -> Tuple[float, List[float], List[float], int]:
  """Divide and conquer algorithm for finding closest-pair of points
  
  Parameters
  ----------
  points : List of points

  Returns
  -------
  Tuple containing the shortest distance, two points forming the closest-pair, and the number
  of euclidian distance operation performed
  """
  # Base case
  if len(points) == 2:
    return euclidean_distance(points[0], points[1]), points[0], points[1], 1
  # Base case
  elif len(points) == 3:
    min_distance, index_1, index_2 = min3(euclidean_distance(points[0], points[1]), 
                                          euclidean_distance(points[0], points[2]), 
                                          euclidean_distance(points[1], points[2]))
    return min_distance, points[index_1], points[index_2], 3
  # Recursive case
  else:
    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]

    # Find the closest-pair of points in the left and right subarray
    min_left, point_left_1, point_left_2, count_left = closest_pair(left)
    min_right, point_right_1, point_right_2, count_right = closest_pair(right)

    # Compare the shortest distance of the left and right subarrray
    min_distance, point_1, point_2 = (min_left, point_left_1, point_left_2) if min_left <= min_right else (min_right, point_right_1, point_right_2)

    # Find the closest-pair of points across both subarray
    min_strip, point_strip_1, point_strip_2, count_strip = closest_pair_strip(left, right, min_distance, point_1, point_2)

    # Compare it to the current shortest distance
    min_distance, point_1, point_2 = (min_strip, point_strip_1, point_strip_2) if min_strip <= min_distance else (min_distance, point_1, point_2)

    count_euc = count_left + count_right + count_strip
    return min_distance, point_1, point_2, count_euc