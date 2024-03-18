"""
def tabuada(n):
    for x in range(11):
        print(f"{n}x{x}=", x * n)
"""
"""
def enesimo(num):
    for x in range(1,num+1):
        for i in range(x):
            print(f"{x}", end=" ")
        print()
"""
"""def enesimo2(num):
    for x in range(1,num):
        for i in range(x+1):
            if (i>0):
                print(f"{i}", end=" ")
        print()
"""
"""def exerc004(num):
    h = num //3600
    hr = num % 3600
    min = hr //60
    s = hr %60
    return h, min, s
"""


def NumPrimo(n):
    if n>0:
        if n % 2 == 0 and n % n == 0:
            return True
        else:
            return False
