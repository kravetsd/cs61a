# coding: utf-8
def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    cnt = min(a,b)
    while (cnt%a==0 and cnt%b==0) is False :
        cnt = cnt+1
    return cnt
