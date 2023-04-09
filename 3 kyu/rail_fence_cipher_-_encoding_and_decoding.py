'''
Create two functions to encode and then decode a string using the Rail Fence 
Cipher. This cipher is used to encode a string by placing each character 
successively in a diagonal along a set of "rails". First start off moving 
diagonally and down. When you reach the bottom, reverse direction and move 
diagonally and up until you reach the top rail. Continue until you reach the
end of the string. Each "rail" is then read left to right to derive the 
encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in 
a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    

The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN

Write a function/method that takes 2 arguments, a string and the number of 
rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and 
the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing 
an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for 
simplicity. There are, however, tests that include punctuation. Don't filter 
out punctuation as they are a part of the string.


https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python
'''

def encode_rail_fence_cipher(string, n):
    encode_list = create_rail_fence_list(string, n)
    
    output = ''
    for line in range(len(encode_list)):
        for letter in encode_list[line]:
            output += letter
    
    return output
    

def decode_rail_fence_cipher(string, n):
    encode_list = create_empty_list(n)
    decode_index_list = create_rail_fence_list(range(len(string)), n)
    
    index_string = 0
    for line in range(n):
        for column in range(len(decode_index_list[line])):
            encode_list[line].append(string[index_string])
            index_string += 1
    
    decode_dict = {}
    for line in range(n):
        for column in range(len(encode_list[line])):
            decode_dict[
                decode_index_list[line][column]] = encode_list[line][column]
    
    output = ''
    for key in sorted(decode_dict):
        output += decode_dict[key]
    
    return output
 
    
def create_empty_list(length):
    return [[] for i in range(length)]
    

def create_rail_fence_list(input, length):
    rail_fence_list = create_empty_list(length)
    direction = 1
    line = 0
    for value in input:
        rail_fence_list[line].append(value)
        line += direction
        if (line == (length - 1)) or (line == 0):
            direction *= -1
            
    return rail_fence_list


if __name__ == "__main__":
    print(f'encode -> "GeeksforGeeks": "{encode_rail_fence_cipher("GeeksforGeeks", 3)}"')
    print(f'decode -> "GsGsekfrekeoe": "{decode_rail_fence_cipher("GsGsekfrekeoe", 3)}"')
 