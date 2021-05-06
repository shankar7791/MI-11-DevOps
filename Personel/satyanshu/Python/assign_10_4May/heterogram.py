# Function to Check whether a given string is Heterogram or not

def heterogram(inp):
    
    inps=set(inp)
    #print (inps)
    if len(inps)==len(inp):
        print ('Yes')
    else:
        print("no")
        
inp = input("enter the string : ")
heterogram(inp)

