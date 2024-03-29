'no imports!'
'no list comprehensions!'
'no lambdas!'
'no inbuild functions!'
'except loops, conditions, return, raise, len, range'


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
    result = []
    while len(result) is not x:
        if start % 2 != 0:
            result.append(start)
        start += 1
    return result


def get_even_numbers(x, stop, z):
    """
    Returns a list containing first 'x' even elements lower than 'stop'.
    That elements must be divisible by 'z'.
    """
    result = []
    counter = 0
    while len(result) is not x:
        if counter % 2 == 0 and counter < stop and counter // z:
            result.append(counter)
        counter += 1
    return result


def get_sum_of_greatest_elements(my_list, x):
    """
    Returns a single integer, which is a sum of 'x' biggest elements from 'my_list'
    i.e. Returns a sum of 3 biggest elements from [2, 18, 5, -11, 7, 6, 9]
    """
    result = []
    for i in range(0, x):
        max1 = 0
        for j in range(len(my_list)):
            if my_list[j] > max1:
                max1 = my_list[j]
        my_list.remove(max1)
        result.append(max1)

    count = 0
    for x in result:
        count += x
    return count


def get_average_of_elements(first_list, second_list):
    """
    Returns a single integer, which is an average from elements that are on 
    'first_list' but not on 'second_list'
    """
    count = 0
    for x in first_list:
        if first_list not in second_list:
            count += x
    return count // len(first_list)


'BONUS'
def return_prime_numbers_less_tahn_100():
    """
    Returns a list containing prime numbers that are less than 100
    """
    primes = []
    for num in range(100):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False 
        if is_prime:
            primes.append(num)
    return primes


def main():
    # TODO first_list, second_list, x, stop, z

    # get_max_common_element(first_list, second_list)
    # get_odd_elements(x, start)
    # get_even_numbers(x, stop, z)
    # get_sum_of_greatest_elements(my_list, x)
    # get_average_of_elements(first_list, second_list)
    print(return_prime_numbers_less_tahn_100())


if __name__ == "__main__":
    main()