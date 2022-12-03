def first():
    second()
    print("I am the first method")

def second():
    third()
    print("I am the second method")

def third():
    fourth()
    print("I am the third method")

def fourth():
    print("I am the fourth method")

# first()

# output
# I am the fourth method
# I am the third method
# I am the second method
# I am the first method

def recurrsiveMethod(n):
    if(n < 1):
        print("n is less than 1")
    else:
        recurrsiveMethod(n-1)
        print(n)

recurrsiveMethod(3)