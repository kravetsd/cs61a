# coding: utf-8
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    cnt = 1
    print(n)
    while n!=1:
        if n%2 == 0:
            n = n/2
            print(int(n))
            cnt = cnt+1
        else:
            n = n*3+1
            print(int(n))
            cnt = cnt+1
    return cnt
