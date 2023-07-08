def create_stack():
    stack=[]
    return stack
#CHECK IF STACK IS EMPTY
def check_empty(stack):
    return len(stack)==0
#push operation to insert an element on top of stack
def push(stack,item):
    stack.append(item)
    print("pushed item: "+item)
#pop operation to remove an element from top of stack
def pop(stack):
    if((check_empty(stack))):
        return "stack is empty"
    return stack.pop()

stack=create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
push(stack,str(5))
print("popped item: "+pop(stack))
print("stack after popping an element: "+str(stack))

    

