credits = int(input('enter how many credits: '))

if credits <= 30:
    print("the student is a freshman")
elif 31 <= credits <= 55:
    print("he is sophomore")
elif 56 <= credits <=85:
    print("he is junior")
else:
    print("he is Senior")

