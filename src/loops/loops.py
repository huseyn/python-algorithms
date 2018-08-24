def print_to_N():
    '''
    Write a program that prints on the console the numbers from 1 to N.
    The number N should be read from the standard input.
    :return:
    '''

    n = int(input('Enter value: '))

    for i in range(0, n):
        print('Hello world')


def print_not_divisible_by_3_7():
    '''
    Write a program that prints on the console the numbers from 1 to N,
    which are not divisible by 3 and 7 simultaneously. The number N
    should be read from the standard input.
    :return:
    '''

    n = int(input('Enter value: '))

    for i in range(0, n):
        if i % 3 != 0 and i % 7 != 0:
            print(i)


def find_smallest():
    n = int(input('Enter count: '))
    arr = []
    max = 0

    for i in range(0, n):
        j = int(input('Enter value: '))
        arr.append(j)
        if max > j:
            max = j

    return max


