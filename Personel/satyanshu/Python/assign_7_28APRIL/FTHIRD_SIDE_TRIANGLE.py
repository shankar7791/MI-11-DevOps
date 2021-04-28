def pythagoras(base,height,hypotenus):
        if base == str("x"):
            height=int(height)
            hypotenus=int(hypotenus)
            return ("base = " + str(((hypotenus**2) - (height**2))**0.5))
        elif height == str("x"):
            base=int(base)
            hypotenus=int(hypotenus)
            return ("height = " + str(((hypotenus**2) - (base**2))**0.5))
        elif hypotenus == str("x"):
            base=int(base)
            height=int(height)
            return ("Hypotenus = " + str(((base**2) + (height**2))**0.5))
        else:
            return "You know the answer!"
print("enter any two side of right angle triangle")
print("enter x for unknown side")   
base=(input("Enter base : "))
height=(input("Enter height : "))
hypotenus=(input("Enter hypotenus : "))
print(pythagoras(base,height,hypotenus))
