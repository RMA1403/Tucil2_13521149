from functions.closest_pair import closest_pair
from functions.sorting import quicksort_on_x
from functions.utility import get_random_points
from functions.visualizer import visualize
from functions.input_output import get_user_input, print_output
from functions.brute_force import brute_force

def main() -> None:
  """Main function for this program"""
  num_points, dimension = get_user_input()
  points = get_random_points(num_points, dimension)

  sorted_points = quicksort_on_x(points)
  min_distance_dnc, point_1_dnc, point_2_dnc = closest_pair(sorted_points)

  min_distance_bf, point_1_bf, point_2_bf = brute_force(points)

  print_output(min_distance_dnc, point_1_dnc, point_2_dnc, 1, min_distance_bf, point_1_bf, point_2_bf, 1, 1.0)

  # visualize(p, p1, p2)

if __name__ == "__main__":
  main()