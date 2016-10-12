# coding: utf-8
def c():
    return True
def t():
    return 1
def f():
    print('something else')
    return 1
def with_if_statement():
        """
        >>> with_if_statement()
        1
        """
        if c():
                return t()
        else:
                return f()
    
with_if_statement()
