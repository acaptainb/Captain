'''
Abdulaziz
'''

def is_between(a, b, c):
    if b <= c <= a or a <= c<= b:
        return True
    else:
        return False

def perform_op(op1, op2, operation):
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

def draw_shape(shape,size):
    pass

if __name__ == "__main__":
    a, b, =map(int,input("put the number here").split())
    # you can put code here to run your functions for testing
    c=input("put the sign here")
    # print(is_between(a,b,c))
    print(perform_op(a,b,c))
    # do not add extra code outside here or the functions you
    # are writing or it may confuse/break the autograder
    pass

