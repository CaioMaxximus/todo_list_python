def add(a,b):
    return a + b

def nop():
    return "oi"

def pool(func,*args):
    return func(*args)


if __name__ == '__main__':
    print(pool(add , 2,2))
    print(pool(nop))