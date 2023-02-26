from typing import List

def euclidean_distance(p1: List[float], p2: List[float]) -> float:
  sum = 0
  for i in range(len(p1)):
    sum += (p1[i]-p2[i])**2
  return sum**(1/2)