import math
import time

def f(x):
  return 4 / (1 + x**2)

def reimann_sum(a, b, n):
  """
  Menghitung nilai integral f(x) dari a sampai b dengan metode integrasi Riemann.

  Args:
    a: Batas bawah integrasi.
    b: Batas atas integrasi.
    n: Jumlah subinterval.

  Returns:
    Nilai integral numerik.
  """
  h = (b - a) / n
  total = 0
  for i in range(n):
    x = a + i * h
    total += f(x)
  return h * total

def main():
  # Nilai referensi pi
  pi_ref = 3.14159265358979323846

  # Variasi nilai N
  n_vals = [10, 100, 1000, 10000]

  for n in n_vals:
    # Hitung integral numerik
    start_time = time.time()
    integral = reimann_sum(0, 1, n)
    end_time = time.time()
    exec_time = end_time - start_time

    # Hitung galat RMS
    error = abs(integral - pi_ref)
    rms_error = math.sqrt(error**2 / n)

    # Tampilkan hasil
    print(f"N = {n}")
    print(f"Integral numerik: {integral}")
    print(f"Galat RMS: {rms_error}")
    print(f"Waktu eksekusi: {exec_time:.2f} detik")
    print()

if __name__ == "__main__":
  main()
