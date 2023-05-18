

from itertools import zip_longest


def mergeStringsAlternatively(w1,w2):
    new_str = ""
    len1 = len(w1)
    len2 = len(w2)
    for i in range(min(len1,len2)):
        new_str += w1[i] + w2[i]
    if(len1 > len2):
        new_str += w1[len2:]
    else:
        new_str += w2[len1:]
    return new_str

def with_zip_longest(w1,w2):
    return "".join(sum(zip_longest(w1,w2,fillvalue=""),()))

def with_zip(w1,w2):
    return "".join([x+y for x, y in zip(w1,w2)]) + w1[min(len(w1), len(w2)):] + w2[min(len(w1),len(w2)):]

print(with_zip("ab","pqrs"))
print(with_zip_longest("ab","xyz"))