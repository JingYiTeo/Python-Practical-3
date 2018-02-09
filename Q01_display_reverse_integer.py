Number = int(input("Please Enter Integer: "))

def reverse_function(n):
    Number = 0
    while n > 0:
        Number *= 10
        Number += n % 10
        n //= 10
    return Number

print("The reverse of {} is {}.".format(Number, reverse_function(Number)))

