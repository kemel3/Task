'no imports!'
'no list comprehensions!'
'no lambdas!'
'no inbuild functions!'
'except loops, conditions, return, raise'


def get_max_common_element(first_list, second_list):
    """
    Select common element from both lists and return one with the max value.

    :raises ValueError: if any of the input lists are empty.
    Error message: 'Input lists cannot be empty'
 
    :raises ValueError: if there are no common elemens.
    Error message: 'There are no common elements'
    """
    if not first_list or not second_list:
        raise ValueError('Input lists cannot be empty')

    result = []
    for elelemt in first_list:
        if elelemt in second_list:
            result.append(elelemt)
    
    max_num = result[0]
    for item in result:
        if item > max_num:
            max_num = item
    
    if not result:
        raise ValueError('There are no common elements')
    
    return max_num


def get_odd_elements(x, start):
    """
    Return a list containing first 'x' odd elements starting from 'start'
    """
    pass


def get_even_numbers(x, stop, z):
    """
    Returns a list containing first 'x' even elements lower than 'stop'.
    That elements must be divisible by 'z'. 
    """
    pass


def get_sum_of_greatest_elements(my_list, x):
    """
    Returns a single integer, which is a sum of 'x' biggest elements from 'my_list'
    i.e. Returns a sum of 3 biggest elements from [2, 18, 5, -11, 7, 6, 9]
    """
    pass


def get_average_of_elements(first_list, second_list):
    """
    Returns a single integer, which is an average from elements that are on 
    'first_list' but not on 'second_list'
    """
    pass


'BONUS'
def return_prime_numbers_less_tahn_100():
    """
    Returns a list containing prime numbers that are less than 100
    """
    pass


def main():
    pass