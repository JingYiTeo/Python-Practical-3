def m_series(i):
    print("\n""i", "\t""m(i)")
    for n in range(1, i+1):
        sum = 0
        for a in range(n+1):
            sum += a / (a+1)
        print("{}".format(n) + "\t{:.4f}".format(sum))

m_series(20)

