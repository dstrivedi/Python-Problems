
import string

def checkDigits(str):
    for s in str:
        if s in string.digits:
            return True
    return False

print(checkDigits("Geeks for geeks")) #False
print(checkDigits("123Hello")) #True