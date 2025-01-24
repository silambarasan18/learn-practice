# Problem: Expand the given string such that each letter is repeated 
# the number of times specified by the digit following it.
# Example:
# Input: "a1b3"
# Output: "abbb"

def expand_string(string):
    result = ""  # Initialize an empty result string
    i = 0  # Start at the first character in the string

    # Iterate through the string
    while i < len(string):
        #check if the current chareacter is a digit
        if string[i].isdigit():
            # initialize count and parse multi-digit numbers
            count =0
            while i < len(string) and string[i].isdigit():
                count = count * 10 + int (string[i]) #build the full number
                i += 1
            char = string[i-len(str(count)) - 1] #get the preceding character
            result += char * count #repeat the charecter ' count' times
        else:
            i += 1 # Move to the next character if it's not a digit
    return result  # Return the expanded string

import re

# Test the function using regular expressions
def expand_string_regex(string):
    #Find all pairs of (letter, number) in the string using regex
    pairs = re.findall(r'([a-zA-Z])(\d+)', string)
    #Expand each pair and concatenate the result
    result = ''.join(char * int(count) for char,count in pairs)
    return result


# Test the function
a = "a102b3"
c = expand_string(a)
print(c) 
c = expand_string_regex(a)
print(c)  # Output: abbb

print(expand_string("a12b3"))    # Output: aaaaaaaaaaaabbb
print(expand_string("x4y21z5"))  # Output: xxxxyyyyyyyyyyyyyyyyyyyzzzzz
print(expand_string("m0n10"))    # Output: nnnnnnnnnn (m is skipped as 0 means no repeats)
print(expand_string(""))         # Output: (empty string)
print(expand_string("p5"))       # Output: ppppp
print(expand_string("q1r"))      # Output: q (invalid format for 'r' is ignored)
print(expand_string("a123"))     # Output: aaaaaaaaaaaaaaaaaaaaaaaaaaaa

