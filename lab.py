import time
import sys
import math

start_time = time.time()

print("Чтение входного файла...")
with open('input.txt', 'r') as file:
    N = int(file.read().strip())
print(f"Входное число N: {N}")

def find_min_divisor(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n

d = find_min_divisor(N)

if d == N:
    A = 1
    B = N - 1
else:
    A = N // d
    B = N - A

current_gcd = math.gcd(A, B)
print(f"A = {A}, B = {B}")
print(f"Наибольший общий делитель (НОД): {current_gcd}")

print("\nЗапись результата в output.txt...")
with open('output.txt', 'w') as file:
    file.write(f"{A} {B}")

end_time = time.time()
elapsed_time = end_time - start_time

try:
    import psutil
    process = psutil.Process()
    memory_used = process.memory_info().rss / 1024
    memory_info = f"Использовано памяти: {memory_used:.2f} KB"
except ImportError:
    memory_info = "Для точного замера памяти установите модуль psutil"

print("\nИтоговая информация:")
print(f"Время выполнения: {elapsed_time:.6f} секунд")
print(memory_info)
print(f"Результат сохранен в output.txt: {A} {B}")

print("\nЗахарова Анастасия Григорьевна 09.03.01ПОВа-o24")
