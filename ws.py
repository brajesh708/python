a=10
b=4

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error: Division by zero is not allowed"
    else:
        return a/b

print("Addition:", add(a,b))
print("Subtraction:", subtract(a, b))

print("Multiplication:", multiply(a, b))

print("Division:", divide(a, b))