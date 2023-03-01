from typing import List, Tuple

def partition(_points: List[List[float]]) -> Tuple[List[List[float]], List[List[float]]]:
  """Parition algorithm for quicksort
  
  Parameters
  ----------
  _points : List of points

  Returns
  -------
  Tuple containing the partitioned list of points
  """
  points = _points[:]
  pivot = points[0]
  i = 1
  j = len(points)

  while i < j:
    if points[i][0] < pivot[0]:
      i += 1
    else:
      j -= 1
      points[i], points[j] = points[j], points[i]
      
  points[i-1], points[0] = points[0], points[i-1]
  return points[:i], points[i:]

def quicksort_on_x(points: List[List[float]]) -> List[List[float]]:
  """Quicksort algorithm for sorting a list of points by its x axis
  
  Parameters
  ----------
  points : List of points

  Returns
  -------
  Sorted list of points ascending by its x axis
  """
  # Base case
  if len(points) <= 1:
    return points
  # Recursive case
  else:
    left, right = partition(points)
    return quicksort_on_x(left) + quicksort_on_x(right)