import numpy as np

line1 = input("Введіть перший масив (числа через пробіл): ")
a = np.array([int(x) for x in line1.split()])

line2 = input("Введіть другий масив (стільки ж чисел): ")
b = np.array([int(x) for x in line2.split()])

print("Масив A:", a)
print("Масив B:", b)

print("Сума:", a + b)
print("Різниця:", a - b)
print("Добуток:", a * b)
print("Частка:", a / b)

c = np.concatenate((a, b))
print("Об'єднаний масив:", c)

print("Максимальний елемент:", c.max())
print("Мінімальний елемент:", c.min())
print("Сума елементів:", c.sum())
print("Добуток елементів:", c.prod())