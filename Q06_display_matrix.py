side = int(input("Please Enter an Integer: "))

import random

random_matrix = [[random.randint(0,1) for j in range(side)] for i in range(side)]
for i in range(side):
    print(random_matrix[i])
