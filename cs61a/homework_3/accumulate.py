# coding: utf-8
identity = lambda x:x
from operator import add, mul

square = lambda x : x*x
def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    if n==0:
        return base
    return combiner(accumulate(combiner,base,n-1,term),term(n))
def summation_using_accumulate(n, term):
    return accumulate(add,0,n,term)
def product_using_accumulate(n,term):
    return accumulate(mul,1,n,term)
