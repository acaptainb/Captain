'''
Abdulaziz
''' 
def is_between(a, b, c):
    '''
    user enters 3 numbers and function replies as true if c value is in equal or greater than a and equal or less than b or c value is greater or equal than b and less and equal than a  values a and b. 
    '''
    if b <= c <= a or a <= c<= b:
        return True
    else:
        return False
    
def perform_op(op1, op2, operation):
    ''' 
  This function performs calculations based on the type of operation (+, −, ×, ÷). 
  If the operation is division ("/") and the second operand is 0, it returns None because the result is undefined.
    otherwise its still None  '''
    if operation not in ['+','-','*','/']:
        return None
    elif operation == '+':
        return op1 + op2
    elif operation == '-':
        return op1 - op2
    elif operation == '*':
        return op1 * op2
    elif operation == '/':
        if op2 == 0:
            return None
        return op1 / op2
    else:
        return None
    

def draw_shape(shape,size):
    ''' If the user puts "circle," the program
      draws a circle based on the size they input.
        If the user puts "triangle," it draws a triangle with the entered size.
    '''
    if shape not in ['circle','triangle']:
        return None
    import turtle as t
    if shape == 'circle':
        t.circle(size)
    elif shape == 'triangle':
            t.forward(size)
            t.left(120)
            t.forward(size)
            t.left(120)
            t.forward(size)
            t.left(120)
    t.done()





if __name__ == "__main__":
    # a, b, =map(int,input("put the number here").split())
    x=int(input("put the number here: "))
    c=input("put the shape here:")
    # print(is_between(a,b,c))
    # print(perform_op(a,b,c))
    print(draw_shape(c,x))
    is_between(1,2,3)
    is_between(3,2,1)
    pass