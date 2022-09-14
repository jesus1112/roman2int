"""
Script that converts a valid roman numeral to an integer
The roman numeral is in the interval [1,3999]

https://leetcode.com/problems/roman-to-integer/
Solution by Jesus Navarro
"""

def romanToInt(s: str) -> int:
    romanToInt_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }
    # Assert s length
    assert len(s) <= 15
    assert len(s) >= 1
    # No need to assert each character since it is garanteed that s is a valid roman numeral
    # and s only contains the characters 'I', 'V', 'X', 'L', 'C', 'D', and 'M'
    num = 0
    for i in range(len(s)):
        # If it's 'I', 'X', or 'C', it's necessary to check if it is subtracting its value to
        # the next character or if it's adding its corresponding value to the result
        # but only if its a valid subtraction ("IV", "IX", "XL", "XC", "CD", "CM")
        if s[i] == 'I' and i < len(s) - 1 and (s[i + 1] == 'V' or s[i + 1] == 'X'):
            num -= romanToInt_dict[s[i]]
        elif s[i] == 'X' and i < len(s) - 1 and (s[i + 1] == 'L' or s[i + 1] == 'C'):
            num -= romanToInt_dict[s[i]]
        elif s[i] == 'C' and i < len(s) - 1 and (s[i + 1] == 'D' or s[i + 1] == 'M'):
            num -= romanToInt_dict[s[i]]
        else:
            # In any other case, the corresponding value is added to the result
            num += romanToInt_dict[s[i]]
    return num


if __name__ == '__main__':
    roman_str = 'MMMCMXCIV'
    print(f'{roman_str} = {romanToInt(roman_str)}')
