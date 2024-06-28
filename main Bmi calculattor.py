
Name = input("Enter your name:")
the_weight = float(input("Enter the weight in kg: "))
the_height = float(input("Enter the height in cm: "))
# defining a function for BMI
the_BMI = the_weight / (the_height/100)**2
# printing the BMI
print("Your Bmi", the_BMI)

if the_BMI > 0:
    if (the_BMI< 18.6):
        print("underweight.youe need ")
    elif (the_BMI <= 22.9):
         print("normal")
    elif (the_BMI <= 24.9):
       print("Overweight.")
    elif(the_BMI <=29.9):
        print("obese1")
    elif(the_BMI >30):
       print("obese2")
    else:
        print("enter the valid input")