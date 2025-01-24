
def string_to_number(string):
    result = 0
    for char in string:
        result = result*10 + (ord(char) - ord('0'))

    return result

num1 = '123'
num2 = '100'
numbint1 =  string_to_number(num1) # Output: 123

numbint2 =  string_to_number(num2) # Output: 100
print(numbint1*numbint2)
