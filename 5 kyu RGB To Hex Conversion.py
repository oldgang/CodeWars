# 5 kyu
# RGB To Hex Conversion
'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''

def decToHex(number):
    if number < 0:
        return '00'
    elif number > 255:
        return 'FF'
    else:
        return hex(number)[2:].upper().zfill(2)

def rgb(r, g, b):
    return decToHex(r) + decToHex(g) + decToHex(b)

# Test Cases
print(rgb(0,0,0)) # '000000'
print(rgb(0,0,-20)) # '000000'
print(rgb(300,255,255)) # 'FFFFFF'
print(rgb(173,255,47)) # 'ADFF2F'
print(rgb(255,255,255)) # 'FFFFFF'

