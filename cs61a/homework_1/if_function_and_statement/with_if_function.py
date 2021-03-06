# coding: utf-8
def  c():
    return True
def t():
    return 1
def f():
    print('something else')
    return 1
def with_if_function():
        return if_function(c(), t(), f())
        
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
    
with_if_function()
