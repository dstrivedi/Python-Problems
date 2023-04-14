# Sample Input

# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output

# 3
# 2 1 1
# Explanation

# There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

n = int(input())
occur = dict()
for i in range(n):
    word = input()
    if word in occur:
        occur[word] += 1
    else:
        occur[word] = 1
print(len(occur))
print(*occur.values())
