# coding: utf-8
def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k%10 == 7:
        return True
    elif k//10 == 0:
        return False
    else:
        k = k//10
        return has_seven(k)
    
