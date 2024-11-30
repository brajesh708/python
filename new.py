tup1=(1, "a" , True)
tup2=(2,4,6)
print(tup1+tup2)

def add_tuples(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1]
            + tup2[1], tup1[2] + tup2[2])
    
    
print(add_tuples(tup1, tup2))


def sum_of_tuple(tup):
    sum = 0
    for i in tup:
        sum += i
    return sum

print(sum_of_tuple(tup1))

def multiply_tuple(tup):
    product = 1
    for i in tup:
        product *= i
    return product

print(multiply_tuple(tup1))
