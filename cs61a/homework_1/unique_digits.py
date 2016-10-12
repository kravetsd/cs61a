# coding: utf-8
def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    n = str(n)
    cnt = 0 
    tmp = list()
    for digit in range(len(n)) :
        if hasdigit(tmp,n[digit]):
            continue
        else: tmp.append(n[digit])
            
    return len(tmp)

def hasdigit(n,k):          
      if str(k) in str(n):
          return True
      else:
          return False

    
