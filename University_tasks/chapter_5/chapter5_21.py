temprature = int(input("enter temprature(Celius): "))
absolute_zero = -273.115
if temprature <= absolute_zero:
    print("that the temperature is invalid because it is below absolute zero")

elif temprature == absolute_zero:
    print("the temperature is absolute 0")
elif absolute_zero < temprature <= 0:
    print("that the temperature is below freezing")
elif temprature == 0:
    print("that the temperature is at the freezing point")
elif 0 < temprature < 100:
    print("hat the temperature is in the normal range")
elif temprature == 100:
    print("that the temperature is at the boiling point.")
elif temprature > 100:
    print("that the temperature is above the boiling point")
