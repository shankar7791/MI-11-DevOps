#prog 4.2.Write a Python program to get the third side of 
# right angled triangle from two given sides.

a=int(input("Enter input one: "))

b=int(input("Enter input two: "))

def pytho(first_side,second_side,hypo):
        if first_side == str("x"):
            return ("First = " + str(((hypo**2) - (second_side**2))**0.5))
        elif second_side == str("x"):
            return ("Second = " + str(((hypo**2) - (first_side**2))**0.5))
        elif hypo == str("x"):
             return ("Hypo = " + str(((first_side**2) + (second_side**2))**0.5))
        else:
            return ("nothing")
    
print(pytho(a,b,'x'))
print(pytho(a,'x',b))
print(pytho('x',a,b))