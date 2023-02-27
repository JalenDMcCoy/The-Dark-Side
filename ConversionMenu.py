
print("Welcome to the converter thingy!")
print("1. Convert inches to centimeters")
print("2. Convert pounds to kilograms")


print("How much do you weigh in pounds?")
userWeightInPounds = float(input())

userWeightInKilograms = round(userWeightInPounds / 2.2, 2)
print("Well, if you weigh " + str(userWeightInPounds) + " pounds, then you weigh " + str(userWeightInKilograms) + " kilograms ")


print("how tall are you in inches?")
userHeightInInches = float(input())

userHeightInCentimeters = userHeightInInches * 2.54

print("well, if you're " + str(userHeightInInches) + " inches tall, then you're " + str(userHeightInCentimeters) + " centimeters tall")