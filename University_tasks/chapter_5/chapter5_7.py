num = int(input("inter number:"))

for i in range(num, num * 6, num):
    print(i, end="---" if i < 5*num else "\n")