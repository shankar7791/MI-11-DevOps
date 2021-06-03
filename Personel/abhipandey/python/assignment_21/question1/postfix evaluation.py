def postfix_evaluation(s):
    
    s=s.split()

    n=len(s)

    stack =[]

    for i in range(n):

        if s[i].isdigit():
    

            stack.append(int(s[i]))

        elif s[i]=="+":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)+int(b))

        elif s[i]=="*":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)*int(b))

        elif s[i]=="/":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)/int(a))

        elif s[i]=="-":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)-int(a))            

    return stack.pop()


s="10 5 4 + 5 * + 50 -"

val=postfix_evaluation(s)

print("the value is " ,val)