# F(1) = 1;
#
# F(n) = F(n − 1)+n
# если
# n > 1

#Если проблема с глубиной рекурсии -
# один из способов
# import sys
# sys.setrecursionlimit(1500)

def F(n):
    if n == 1:
        return 1
    else:

            return F(n-1)+n



a = F(1000)
print(a)