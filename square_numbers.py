def square_numbers1():
    """ Computes square numbers

    :return: list of square numbers
    """
    return [number*number for number in xrange(1,2001)]

print square_numbers1()


def square_numbers2():
    """ Computes square numbers with use of generator

    :return: generator of square numbers
    """
    for number in xrange(1,2001):
    	yield number*number

print list(square_numbers2())

# or
for number in square_numbers2():
	print number

