'''
>>> JAAR
>>> 07/23/2023
>>> Practicing Fundamentals Program 8
>>> Version 1
'''

'''
>>> Generates a program that will print the multiplication table for a number and will then print the factorial for the number. Afterwards, the program will generate the sum for each pair.
'''

def verify_numbers()-> int :
    '''
    >>> Ensures the user input is a positive integer. Otherwise, will ask for another input.

    >>> Return: (int) number
    '''
    while True :
        try:
            number = int(input())
            if number < 0 :
                raise TypeError
        except ValueError :
            print('\nYour input was invalid.\n\n\tEnter an integer: ', end = '')
        except TypeError :
            print('\n\n\tEnter an integer greater than zero: ', end = '')
        else :
            return number

def factorial(number : int) -> int :
    '''
    >>> Takes an integer and will calculate the factorial for it.

    >>> Param: (int) number
    >>> Return: (int) answer
    '''
    answer = 1
    if 0 < number :
        for i in range(1, number + 1) :
            answer *= i
    return answer

def main() :
    print('Enter an integer: ', end = '')
    number = verify_numbers()
    m_table = {i : int(number/i) for i in range(1, abs(number) + 1) if number/i == int(number/i)}

    print("Multiplication Table:")
    for key, value in m_table.items() :
        print(f'\t({key}, {value})')

    print('\nSum of Pairs in Multiplication Table:')
    for key, value in m_table.items() :
        print(f'\t{ key } + { value } = { key + value }')

    factorial_answer = factorial( number )
    print(f'\nFactorial: { factorial_answer }')

if __name__ == '__main__' :
    main()