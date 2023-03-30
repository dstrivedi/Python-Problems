def fizzBuzz(n:int) -> str:
    """
        Play fizzbuzz
        :param number: The number to check.
        :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if(n % 3 == 0 and n % 5 == 0):
        return "fizz buzz"
    elif(n % 3 == 0):
        return "fizz"
    elif(n % 5 == 0):
        return "buzz"
    else:
        return str(n)

for i in range(1,101):
    print(fizzBuzz(i))