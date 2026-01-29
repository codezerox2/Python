T = int(input("inter temperature: "))

if T > 30:
    print("very hot")
elif 25 < T <= 30:
    print("hot")
elif 20 <= T <=25:
    print("warm")
elif 0 < T <= 10:
    print("cold")
else:
    print("very cold")