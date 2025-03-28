# Отчёт по 1 лабораторной работе

## Задание
![image](https://github.com/user-attachments/assets/d3ba1757-5a16-4cb6-ab1a-f6618ccb7450)

## Зависимости
- Python 3.x
- Опционально: `psutil` для замера памяти  
  ```bash
  pip install psutil
  ```

---

## Результаты тестирования
![image](https://github.com/user-attachments/assets/8e057381-0b3f-4895-a8e3-f25c566367c3)

## Код программы

```Python
import time
import sys

start_time = time.time()

print("Чтение входного файла...")
with open('input.txt', 'r') as file:
    N = int(file.read().strip())
print(f"Входное число N: {N}")

print("\nВычисление A и B...")
if N % 2 == 0:
    A = N // 2
    B = N // 2
else:
    A = (N - 1) // 2
    B = (N + 1) // 2

print(f"A = {A}, B = {B}")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

current_gcd = gcd(A, B)
print(f"Наибольший общий делитель (НОД): {current_gcd}")

print("\nЗапись результата в output.txt...")
with open('output.txt', 'w') as file:
    file.write(f"{A} {B}")

end_time = time.time()
elapsed_time = end_time - start_time

try:
    import psutil
    process = psutil.Process()
    memory_used = process.memory_info().rss / 1024  # в килобайтах
    memory_info = f"Использовано памяти: {memory_used:.2f} KB"
except ImportError:
    memory_info = "Для точного замера памяти установите модуль psutil"

print("\nИтоговая информация:")
print(f"Время выполнения: {elapsed_time:.6f} секунд")
print(memory_info)
print(f"Результат сохранен в output.txt: {A} {B}")

print("\nЗахарова Анастасия Григорьевна 09.03.01ПОВа-o24")

```
