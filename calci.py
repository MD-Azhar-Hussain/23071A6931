def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

x, y = map(int, input("Enter two numbers: ").split())
print("Addition is",add(x,y))
print("Subtraction is",sub(x,y))
print("Multiplication is",mul(x,y))
print("Division is",div(x,y))
