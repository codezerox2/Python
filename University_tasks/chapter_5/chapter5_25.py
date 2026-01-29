count = 0
for i in range(1, 100):
    idk = str(i ** 2)
    if idk[-1] == "4":
        count += 1
    else:
        pass

print(count)