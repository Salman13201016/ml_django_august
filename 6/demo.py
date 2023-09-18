a = 10
b = 20
c = 30

def print_globals():
    print(a, b, c)
    c = 100
    print(c)
print_globals()
