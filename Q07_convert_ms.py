
Time = int(input("Please enter time in milliseconds: "))

def convert_ms(n):
    Secs = int((n / 1000) % 60)
    Mins = int((n / (1000*60)) % 60)
    Hr = int((n / (1000*60*60)))
    return("{}:{}:{}".format(Hr, Mins, Secs))

print(convert_ms(Time))
