from typing import List, Tuple

def partition(_points: List[List[float]]) -> Tuple[List[List[float]], List[List[float]]]:
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
  if len(points) <= 1:
    return points
  else:
    left, right = partition(points)
    return quicksort_on_x(left) + quicksort_on_x(right)