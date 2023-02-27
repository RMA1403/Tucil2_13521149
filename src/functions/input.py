from typing import List, Tuple

def getUserInput() -> Tuple[int, int]:
  print(37*"=")
  print("TUGAS KECIL STRATEGI ALGORITMA")
  print(37*"=")

  num_points = int(input("Masukkan jumlah titik: "))
  dimension = int(input("Masukkan dimensi dari setiap titik: "))

  return num_points, dimension

def printOutput(min_distance_dnc: float, point_1_dnc: List[float], point_2_dnc: List[float], count_ops_dnc: int, min_distance_bf: float, point_1_bf: List[float], point_2_bf: List[float], count_ops_bf: int, exec_time: float) -> None:
  print(50*"=")
  print("ALGORITMA BRUTE FORCE")
  print("Jarak terpendek: ", min_distance_bf)
  print("Titik 1: ", point_1_bf)
  print("Titik 2: ", point_2_bf)
  print("Jumlah operasi euclidean distance: ", count_ops_bf)
  print(50*"=", "\n")

  print(50*"=")
  print("ALGORITMA DIVIDE AND CONQUER")
  print("Jarak terpendek", min_distance_dnc)
  print("Titik 1: ", point_1_dnc)
  print("Titik 2: ", point_2_dnc)
  print("Jumlah operasi euclidean distance: ", count_ops_dnc)
  print(50*"=", "\n")

  print(f"Waktu eksekusi algoritma divide and conquer: {exec_time:.2f} detik")