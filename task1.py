inp = input("Введіть числа через пробіл: ")
B = [int(x) for x in inp.split()]

is_decreasing = True
for i in range(len(B) - 1):
    if B[i] <= B[i+1]:
        is_decreasing = False
        break

new_list = []
if not is_decreasing:
    for x in B:
        if x < 0:
            new_list.append(1)
        else:
            new_list.append(x)
else:
    new_list = list(B)

print(new_list)