from typing import List, Tuple

def get_user_input() -> Tuple[int, int]:
  print(40*"=")
  print("TUGAS KECIL STRATEGI ALGORITMA")
  print(40*"=")

  num_points = int(input("Masukkan jumlah titik: "))
  dimension = int(input("Masukkan dimensi dari setiap titik: "))

  return num_points, dimension

def print_output(min_distance_dnc: float, point_1_dnc: List[float], point_2_dnc: List[float], count_ops_dnc: int, exec_time_dnc: float, min_distance_bf: float, point_1_bf: List[float], point_2_bf: List[float], count_ops_bf: int, exec_time_bf: float) -> None:
  print("\n", 50*"=", sep="")
  print("ALGORITMA BRUTE FORCE")
  print("Jarak terpendek: ", min_distance_bf)
  print("Titik 1: ", end="")
  print_titik(point_1_bf)
  print("Titik 2: ", end="")
  print_titik(point_2_bf)
  print("Jumlah operasi euclidean distance: ", count_ops_bf)
  print(f"Waktu eksekusi algoritma: {exec_time_bf:.5f} detik")
  print(50*"=", "\n")

  print(50*"=")
  print("ALGORITMA DIVIDE AND CONQUER")
  print("Jarak terpendek: ", min_distance_dnc)
  print("Titik 1: ", end="")
  print_titik(point_1_dnc)
  print("Titik 2: ", end="")
  print_titik(point_2_dnc)
  print("Jumlah operasi euclidean distance: ", count_ops_dnc)
  print(f"Waktu eksekusi algoritma: {exec_time_dnc:.5f} detik")
  print(50*"=", "\n")


def print_titik(point: List[float]) -> None:
  print("(", end="")
  for i in range(len(point)-1):
    print(f"{point[i]:.2f},", end="")
  print(f"{point[-1]:.2f})")