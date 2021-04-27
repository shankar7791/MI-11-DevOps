height = float(input("Input your height in inches : "))
weight = float(input("Input your weight in inches : "))
bmi = round(weight / (height ** 2), 2)
print(f"Your BMI is: {bmi}")