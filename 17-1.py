# F(0) = 0;
# F(n) = F(n − 1) + 1, если n > 0 и при этом n mod 3 = 2;
# F(n) = F((n − n mod 3) / 3), если n > 0 и
# при этом n mod 3 < 2.

def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 2:
        return F(n - 1) + 1
    if n > 0 and (n % 3) < 2:
        return F((n - n % 3) / 3)

for i in range(0, 10000):
    if F(i) == 5:
        print(i)
