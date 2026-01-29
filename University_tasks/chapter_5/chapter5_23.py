print("welcome to shop sir \nthe item cost 12$")
print("but there offer if you buy between 10 and 99 the cost will be 10$ per item")
print("and if you want more then 100 will be 7$")
count = int(input("how many you want: "))

if count < 10:
    print(f"the cost will be: {count * 12}")
elif 10 <= count <= 99:
    print(f"the cost will be: {count * 10}")
else:
    print(f"the cost will be {count * 5}")