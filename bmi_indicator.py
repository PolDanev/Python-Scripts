height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
print()
bmi = round(weight / (height * height))

if bmi < 18.5:
  print(f"Your BMI is {bmi} points, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi} points, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi} points, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi} points, you are obese.")
else:
  print(f"Your BMI is {bmi} points, you are clinically obese.")



