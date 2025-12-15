import matplotlib.pyplot as plt

with open("lab_text.txt", "r") as f:
    content = f.read().lower()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
counts = []

for v in vowels:
    counts.append(content.count(v))

plt.bar(vowels, counts, color='pink')
plt.title("Кількість голосних літер")
plt.xlabel("Літера")
plt.ylabel("Кількість")

plt.savefig("result.png")
plt.show()