# Текстовый файл состоит не более чем из 106 символов L, D и R.
# Определите длину самой длинной последовательности,
# состоящей из символов L. Хотя бы один символ L находится
# в последовательности.
# Для выполнения этого задания следует написать программу.

with open("zadanie24_2.txt", "r") as f:
    data = f.read().strip("\n")

data = data.replace("D", ":").replace("R", ":").split(":")
print(data, len(max(data)))


