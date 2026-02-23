# get temperature and unit
temperature = int(input("enter temperature: "))
unit = input("enter the unit F/C: ").upper()
#convert the unit
F = 9/5*(temperature+32)
C = 5/9*(temperature-32)

# check the unit user chose
if unit == "C":
    print(F)
elif unit == "F":
    print(C)
else:
    print("please inter correct unit")
