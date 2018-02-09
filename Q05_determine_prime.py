import math

def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n > 2:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
            
        return True


primelist = []
i = 2
while len(primelist) < 1000:
    if prime(i) == True:
        primelist.append(i)
    i += 1

for idx, p in enumerate(primelist, start=1):
    print("{}\t".format(p), end="")
    if idx % 10 == 0:
        print()

