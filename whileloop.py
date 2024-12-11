i=1
while i<=10:
    print(i,"brajesh mewada")
    i=i+1
    
    
a=10
while a>=1:
    print(a,"hello")
    a=a-1
    
print("Test case 2: Strings with multiple words")

s = "Hello World!"
print(s)  # Output: Hello World!
print(s[0])  # Output: H

print(s[0::2])  # Output: Hlo

print(s[1::2])  # Output: eWl


# some more functions
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))