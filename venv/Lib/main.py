# build Pascal's Triangle
def fact(n):
    if n == 0:
        return 1
    else:
        return  n * fact(n-1)

def choose(n, k):
    return fact(n)/(fact(k) * fact (n-k))

def pascalTriangle(depth):
    coefficient = 0;

    for n in range(depth):

        for x in range(n):
            coefficient = choose(n,x)
            print(coefficient, end= " "),
        print('1.0')


print(pascalTriangle(100))