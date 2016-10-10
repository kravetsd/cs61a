# coding: utf-8
def a_plus_abs_b(a,b):
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b<0:
        f = sub(a,b)
    else:
        f = add(a,b)
    return f
from operator import add, sub
