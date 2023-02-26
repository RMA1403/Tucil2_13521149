from typing import List

def euclidean_distance(p1: List[float], p2: List[float]) -> float:
  sum = 0
  for i in range(len(p1)):
    sum += (p1[i]-p2[i])**2
  return sum**(1/2)

def min3(f1: float, f2: float, f3: float) -> float:
  if f1 <= f2 and f1 <= f3 :
    return f1
  elif f2 <= f1 and f2 <= f3 :
    return f2
  else:
    return f3