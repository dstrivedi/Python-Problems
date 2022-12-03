def palindrome(str): 
    #reverse string and compare with original string
    #reverse string -> str[::-1]
    if str == str[::-1]: 
        print(str + " - String is palindrom")
    else:
        print(str + " - String is not palindrom") 

print(''.join(reversed('KhoKho')))
palindrome('KhoKho')
palindrome('amaama')


def symmetrical(str):
    #check string length is even or odd
    first_str = ""
    second_str = ""
    half = len(str)//2
    if len(str) % 2 == 0: #even
        first_str = str[:half]
        second_str = str[half:]
    else: #odd
        first_str = str[:half]
        second_str = str[half+1:]
    
    if(first_str == second_str):
        print(str + " - String is symmetrical")
    else:
        print(str + " - String is not symmetrical")


symmetrical('KhoKho')