num = int(input("inter num: "))
result = 0

for i in range(1, num+1):
    if num % i == 0:
        result += i
        print(result)
    else:
        pass

print(result)