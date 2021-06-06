def isEmpty(stack):
   if stack==[]:
      return True
   else:
      return False

def Push(stack,item):
   stack.append(item)
   top=len(stack)-1

def Pop(stack):
   if isEmpty(stack):
      print("Underflow")
   else: 
      item=stack.pop()
      if len(stack)==0:
         top=None
      else:
         top=len(stack)
         print("Popped item is "+str(item))

def Display(stack):
   if isEmpty(stack):
      print("Stack is empty")
   else:
      top=len(stack)-1
      print("Elements in the stack are: ")
      for i in range(top,-1,-1):
         print (str(stack[i]))

if __name__ == "__main__":
   stack=[]
   top=None
   Push(stack,10)
   Push(stack,20)
   Push(stack,30)
   Push(stack,40)
   Push(stack,60)
   Pop(stack)

   
   Display(stack)