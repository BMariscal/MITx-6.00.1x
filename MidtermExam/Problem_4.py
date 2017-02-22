#  Problem 4
# 10.0/10.0 points (graded)

# Implement a function called closest_power that meets the specifications below.

# def closest_power(base, num):
#     '''
#     base: base of the exponential, integer > 1
#     num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.
#     '''
#     # Your code here

# For example,

#     closest_power(3,12) returns 2
#     closest_power(4,12) returns 2
#     closest_power(4,1) returns 0

# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    minimum =[]
    maximum=[]

    for i in range(0,11):
        if base**i <= num:
            minimum.append(i)
        elif base**i > num:
            maximum.append(i)
    a=max(minimum)
    b=min(maximum)
    
    if (num - base**a < base**b - num):
        return a
    elif (num - base **a > base**b - num):
        return b
    else:
        return a



    
# Test: closest_power(4, 160.0)

# Output:

#     3

