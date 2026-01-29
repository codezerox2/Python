count = 0

for i in range(100):
    idk = str(i ** 2)
    if  idk[-1]== "1":
        count += 1
    else:
        pass

print(count)