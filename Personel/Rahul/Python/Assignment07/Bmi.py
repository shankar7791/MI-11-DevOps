h = float(input("Enter height in cm : "))
w = float(input("Enter weight in kg : "))

def bmi(h,w):

	BMI = w / (h/100)**2
	print(f"The BMI is - {BMI}")
	if BMI <= 18.4:
	    print("You are underweight.")
	elif BMI <= 24.9:
	    print("You are healthy.")
	elif BMI <= 29.9:
	    print("You are over weight.")
	elif BMI <= 34.9:
	    print("")
	elif BMI <= 39.9:
	    print("You are obese.")
	else:
	    print("")
bmi(h,w)	    