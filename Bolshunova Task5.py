# Multiparadigmatic  programming languages:Task_3
# Bolshunova Kateryna:IKM-221a
print('Multiparadigmatic  programming languages:Task_3\nBolshunova Kateryna:IKM-221a')

# part 1
eps = 1e-4  # задана точність
n = 1  # номер члена ряду
a = 0  # початкове значення суми ряду
prev_a = 0  # попереднє значення суми
while abs(a - prev_a) > eps:
    prev_a = a
    a += 1 / (2*n) + 1 / (3*n)
    n += 1

print("Сума ряду:", a)

# part 2
n = int(input("Введіть ціле число: "))
count = 0  # кількість цифр
while n != 0:
    count += 1
    n //= 10
print("Кількість цифр у введеному числі:", count)

# part 3
a = float(input("Введіть додатне число: "))
eps = 1e-4  # задана точність
x = a / 2  # початкове наближення
while abs(x * x - a) > eps:
    x = 0.5 * (x + a / x)
print("Квадратний корінь числа", a, "дорівнює", x)