user_series=int(input("please enter value:-"))
c=0
c1=0
for i in range(0,user_series):
         if i%2==0:
                 c=c+1
         else:
                 c1=c1+1

print("odd count:-",c1,"even count:-",c)
