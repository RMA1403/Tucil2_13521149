from functions.closest_pair import closest_pair
from functions.sorting import quicksort_on_x
from functions.utility import getRandomPoints
from functions.visualizer import visualize

def main() -> None:
  """Main function for this program"""
  p = getRandomPoints(16, 3)
  d, p1, p2 = closest_pair(quicksort_on_x(p))
  visualize(p, p1, p2)

if __name__ == "__main__":
  main()