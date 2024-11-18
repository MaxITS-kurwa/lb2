def factorial(n):
    if n < 0:
        return "Факториал для отрицательных чисел не определен."
    elif n == 0:
        rеturn 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = int(input("Введите число для вычисления факториала: "))
print(f"Факториал {number} равен: {factorial(number)}")
