from typing import List, Tuple
from random import uniform

def euclidean_distance(p1: List[float], p2: List[float]) -> float:
  sum = 0
  for i in range(len(p1)):
    sum += (p1[i]-p2[i])**2
  return sum**(1/2)

def min3(f1: float, f2: float, f3: float) -> Tuple[float, int, int]:
  if f1 <= f2 and f1 <= f3 :
    return f1, 0, 1
  elif f2 <= f1 and f2 <= f3 :
    return f2, 0, 2
  else:
    return f3, 1, 2

def getRandomPoints(num_points: int, dimension: int) -> List[List[float]]:
  return [[uniform(-500, 500) for _ in range(dimension)] for _ in range(num_points)]