# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих
# подряд пар символов вида
# согласная + гласная.
import re

with open("24.txt", "r") as f:
    data = f.read().strip("\n")

print(data)



#
# data = data.replace("D", ":").replace("R", ":").split(":")
# print(data, len(max(data)))