from time import time

from functions.closest_pair import closest_pair
from functions.sorting import quicksort_on_x
from functions.utility import get_random_points
from functions.visualizer import visualize
from functions.input_output import get_user_input, print_output
from functions.brute_force import brute_force

def main() -> None:
  """Main function for this program"""

  # Initialize points from user input
  num_points, dimension = get_user_input()
  points = get_random_points(num_points, dimension)

  # Sort points using quicksort
  sorted_points = quicksort_on_x(points)

  # Find closest-pair using divide and conquer
  start_time_dnc = time()
  min_distance_dnc, point_1_dnc, point_2_dnc, count_euc_dnc = closest_pair(sorted_points)
  end_time_dnc = time()

  # Find closest-pair using brute force
  start_time_bf = time()
  min_distance_bf, point_1_bf, point_2_bf, count_euc_bf = brute_force(points)
  end_time_bf = time()

  # Calculate execution time of each algorithms
  exec_time_dnc = end_time_dnc - start_time_dnc
  exec_time_bf = end_time_bf - start_time_bf

  # Print the results to the screen
  print_output(min_distance_dnc, point_1_dnc, point_2_dnc, count_euc_dnc, exec_time_dnc, min_distance_bf, point_1_bf, point_2_bf, count_euc_bf, exec_time_bf)

  # If the points are three dimensional, visualizes it
  if dimension == 3:
    visualize(points, point_1_dnc, point_2_dnc)

if __name__ == "__main__":
  main()