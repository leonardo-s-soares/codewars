'''
Write Number in Expanded Form

You will be given a number and you will need to return it as a string
in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

Note: All numbers will be whole numbers greater than 0.
'''

def expanded_form(num):
    digits = list(map(int, str(num)))
    for index, digit in enumerate(digits):
        digits[index] = (digit * (10 ** (len(digits) - (index + 1))))
    
    num_expanded_form = ''
    for digit in digits:
        if digit == 0:
            continue
        num_expanded_form += f'{digit} + '
        
    return num_expanded_form.rstrip(' + ')
