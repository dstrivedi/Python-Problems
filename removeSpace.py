# Remove spaces from a string
from multiprocessing.reduction import steal_handle


str = "g ee k g e ek"
new_str = [ch for ch in str if(ch!=" ")]
# for ch in str:
#     if(ch != " "):
#         new_str = new_str +  ch

print(str.replace(' ',''))
print("".join(new_str))