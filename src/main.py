from functions.closest_pair import closest_pair
from functions.sorting import quicksort_on_x

def main() -> None:
  """Main function for this program"""
  p = [
    [13.0, 13.0, 13.0],
    [11.0, 11.0, 11.0],
    [10.0, 10.0, 10.0],
    [8.0, 8.0, 8.0],
    [6.0, 6.0, 6.0],
    [4.0, 4.0, 4.0],
    [2.0, 2.0, 2.0],
    [0.0, 0.0, 0.0],
  ]
  print(closest_pair(quicksort_on_x(p)))
if __name__ == "__main__":
  main()