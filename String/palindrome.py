from tokenize import String


def word_is_palindrome(str):
    return str.casefold() == str[::-1].casefold()

def sentence_is_palindrome(sentence):
    
    # docstring using """ """
    """_summary_
    
    This function checks whether the sentence is palindrome or not.
    
    Args:sentence should be type of String which can be passed as params.
        sentence (_type_): _description_
    
    Returns:sentence with reverse order to check palindrome.
        _type_: _description_
    """
    # print docstring of function
    print(sentence_is_palindrome.__doc__)
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return word_is_palindrome(string)

print(word_is_palindrome("Radar"))
print(word_is_palindrome("python"))

print(sentence_is_palindrome("Was it a car, or a cat, I saw"))