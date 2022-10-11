# F(1) = 1;
#
# F(n) = F(n − 1)+n
# если
# n > 1


def F(n):
    if n == 1:
        return 1
    else:
        try:
            return F(n-1)+n
        except:
            pass

a = F(4000)
print(a)