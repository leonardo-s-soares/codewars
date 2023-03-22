'''
Create a function taking a positive integer between 1 and 3999 (both included)
as its parameter and returning a string containing the Roman Numeral 
representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero. In Roman
numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 
is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in 
descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'

Help:
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

Remember that there can't be more than 3 identical symbols in a row.
More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
'''

def convert_int_to_roman_numerals(num):
    roman_dict = {
        1:'I',
        5:'V',
        10:'X',          
        50:'L',
        100:'C',
        500:'D',
        1_000:'M'
    }

    digits = separate_digits(num)
    roman_num = ''    
    for digit in digits:
        len_digit = len(str(digit))
        tenth = calculate_tenth(len_digit) 
         
        if is_between_1s_and_3s(digit, tenth):
            roman_num += roman_dict[tenth] * (digit // tenth) 
        elif is_between_6s_and_8s(digit, tenth):
            roman_num += roman_dict[5 * tenth]    
            roman_num += roman_dict[tenth] * ((digit - (5 * tenth)) // tenth)
        elif is_4s(digit, tenth):
            roman_num += roman_dict[tenth]
            roman_num += roman_dict[5 * tenth]          
        elif is_9s(digit, tenth):
            roman_num += roman_dict[tenth]
            roman_num += roman_dict[10 * tenth]    
        elif is_5s_or_10s(digit):
            roman_num += roman_dict[digit]
            
    return roman_num


def is_between_1s_and_3s(digit, tenth):
    return (digit >= tenth) and (digit <= (3 * tenth))
 
       
def is_between_6s_and_8s(digit, tenth):
    return (digit >= (6 * tenth)) and (digit <= (8 * tenth))


def is_4s(digit, tenth):
    return digit == (4 * tenth)


def is_9s(digit, tenth):
    return digit == (9 * tenth)


def is_5s_or_10s(digit):
    return (digit % 5) == 0


def separate_digits(num):
    numbers = list(map(int, str(num)))  
    for index, digit in enumerate(numbers):
        numbers[index] = (digit * (10 ** (len(numbers) - (index + 1))))
        
    for number in reversed(range(len(numbers))):
        if numbers[number] == 0:
            del numbers[number]
            
    return numbers
    

def calculate_tenth(length):
    return 10 ** (length - 1)
    
 