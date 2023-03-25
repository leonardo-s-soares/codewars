'''
Description:

How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe 
you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes
on USENET.

For this task you're only supposed to substitute characters. Not 
spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> 
"Guvf vf zl svefg EBG13 rkprepvfr!"

'''

def rot13(message=''):
    result = ''
    key = 13
    a_ascii, z_ascii = 65, 90
    for letter in message:    
        if letter.isalpha():
            ascii = ord(letter.upper())
            cipher = ascii + key
            
            if (cipher > z_ascii):
                cipher = ((cipher + key) % 26) + a_ascii
            
            if letter.islower():
                result += chr(cipher).lower()
            else:
                result += chr(cipher) 
        else:
            result += letter
    return result
