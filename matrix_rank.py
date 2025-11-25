#!/usr/bin/env python3
"""
Вычисление ранга матрицы методом приведения к ступенчатому виду (gaussian elimination).
Ввод: N M, затем N строк по M чисел.
"""
def rank_of_matrix(A):
    # Копируем
    A = [row[:] for row in A]
    n = len(A)
    m = len(A[0]) if A else 0
    rank = 0
    EPS = 1e-12
    row = 0
    for col in range(m):
        # Найти непустой ведущий элемент
        sel = None
        for i in range(row, n):
            if abs(A[i][col]) > EPS:
                sel = i
                break
        if sel is None:
            continue
        # swap
        A[row], A[sel] = A[sel], A[row]
        # normalize
        pivot = A[row][col]
        for j in range(col, m):
            A[row][j] /= pivot
        # eliminate
        for i in range(n):
            if i != row:
                factor = A[i][col]
                if abs(factor) > EPS:
                    for j in range(col, m):
                        A[i][j] -= factor * A[row][j]
        row += 1
        rank += 1
        if row == n:
            break
    return rank

def main():
    while True:
        try:
            n,m = map(int, input("Введите N M: ").split())
            if n<=0 or m<=0:
                print("Положительные размерности.")
                continue
            break
        except:
            print("Ошибка ввода.")
    A = []
    for i in range(n):
        while True:
            parts = input(f"Строка {i+1} ({m} чисел через пробел): ").strip().split()
            if len(parts) != m:
                print("Неверное кол-во чисел.")
                continue
            try:
                A.append([float(x) for x in parts])
                break
            except:
                print("Ошибка формата.")
    r = rank_of_matrix(A)
    print("Ранг матрицы:", r)

if __name__ == "__main__":
    main()
