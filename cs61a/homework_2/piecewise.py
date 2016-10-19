# coding: utf-8
def square(x):
        return x * x
def triple(x):
        return 3 * x
def identity(x):
        return x
def increment(x):
        return x + 1
def piecewise(f, g, b):
        """Returns the piecewise function h where:
    
        h(x) = f(x) if x < b,
               g(x) otherwise
    
        >>> def negate(x):
        ...     return -x
        >>> abs_value = piecewise(negate, identity, 0)
        >>> abs_value(6)
        6
        >>> abs_value(-1)
        1
        """
        def h(x):
            if x < b :
                return f(x)
            else:
                return g(x)
        return h    
