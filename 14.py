# Сколько единиц содержится в двоичной записи
# значения выражения
# : 4**2020 + 2**2017 – 15?

def to_sistema(chislo, sistema, count_data):
    answer = ""
    while chislo != 0:
        answer += str(chislo % sistema)
        chislo = chislo // sistema
    print(answer[::-1])
    answer = answer[::-1].count(str(count_data))
    print(answer)

# # bin -2, oct-8, hex-16
# data = 4**2020 + 2**2017 - 15
# data = bin(data)[2:].count("1")
# print(data)

data = 1234**2020 + 3456**2017 - 15
to_sistema(data, 9, 3)
