#!/usr/bin/env python3
"""
Ввод матрицы NxM с клавиатуры и вычисление сред. арифметического
по каждой строке и по каждому столбцу. Пример ввода:
  Введите N M: 2 3
  Введите ряд 1 (через пробел): 1 2 3
  Введите ряд 2 (через пробел): 4 5 6
"""
def read_ints(prompt):
    while True:
        try:
            parts = input(prompt).strip().split()
            nums = [float(x) for x in parts]
            return nums
        except Exception as e:
            print("Ошибка ввода, повторите.")

def main():
    while True:
        try:
            n,m = map(int, input("Введите N M: ").split())
            if n<=0 or m<=0:
                print("N и M > 0")
                continue
            break
        except:
            print("Ошибка. Введите два целых числа через пробел.")
    mat = []
    for i in range(n):
        while True:
            row = input(f"Введите ряд {i+1} ({m} чисел через пробел): ").strip().split()
            if len(row) != m:
                print(f"Нужно {m} чисел.")
                continue
            try:
                mat.append([float(x) for x in row])
                break
            except:
                print("Ошибка числового формата.")
    # Считаем средние
    row_avgs = [sum(r)/len(r) for r in mat]
    col_avgs = []
    for j in range(m):
        s = sum(mat[i][j] for i in range(n))
        col_avgs.append(s/n)
    print("\nСреднее по каждой строке:")
    for i,a in enumerate(row_avgs, start=1):
        print(f"Строка {i}: {a}")
    print("\nСреднее по каждому столбцу:")
    for j,a in enumerate(col_avgs, start=1):
        print(f"Столбец {j}: {a}")

if __name__ == "__main__":
    main()
