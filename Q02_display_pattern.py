Pa = int(input("Please enter a positive integer: "))

def Pattern(n):
    for i in range(n,0,-1):
        print((i-1)*"\t",end="")
        for j in range(n-i+1, 0, -1):
            print(j,end="\t")
        print()
print(Pattern(Pa))





