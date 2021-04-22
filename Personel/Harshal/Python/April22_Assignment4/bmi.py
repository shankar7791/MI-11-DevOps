height = float(input("Input your height : "))
weight = float(input("Input your weight : "))
bmi = round(weight / (height ** 2), 2)
print(f"Your BMI is: {bmi}")