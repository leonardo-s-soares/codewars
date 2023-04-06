'''
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
Examples

to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
1000 -> "M"
 400 -> "CD"
  90 -> "XC"
  40 -> "XL"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      -> 400
"XC"      -> 90
"XL"      -> 40
"I"       -> 1
'''

class RomanNumerals:
    roman_numbers = {
                1_000:'M',
                900:'CM',
                500:'D',
                400:'CD',
                100:'C',
                90:'XC',
                50:'L',
                40:'XL',
                10:'X',
                9:'IX',
                5:'V',
                4:'IV',
                1:'I',
            }
    
    @staticmethod
    def to_roman(val):
        output = ''
        roman_numbers = RomanNumerals.roman_numbers
        for number in roman_numbers:
            while val >= number:
                output += roman_numbers[number]
                val -= number
        return output
    

    @staticmethod
    def from_roman(roman_num):
        roman_numbers = {
            value:key for key, value in RomanNumerals.roman_numbers.items()
            }
        
        len_roman_num = len(roman_num)
        output = 0
        index = 0
        while index < len_roman_num:
                if (index < len_roman_num -1) and (
                        (roman_num[index:index +2]) in roman_numbers):
                    output += roman_numbers[roman_num[index:index +2]]
                    index += 2
                else:
                    output += roman_numbers[roman_num[index]]
                    index += 1
                 
        return output

    