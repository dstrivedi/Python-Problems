ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

def commonElements(l1,l2,l3):
    set_l1 = set(l1)
    set_l2 = set(l2)
    set_l3 = set(l3)
    intersection_l1_l2 = set_l1.intersection(set_l2)
    final_set = intersection_l1_l2.intersection(set_l3)
    return final_set;

def alternate(l1,l2,l3):
    common = set()
    for ele in l1:
        if ele in l2 and ele in l3:
            common.add(ele)
    return common
    # return [ele for ele in l1 if ele in l2 and ele in l3]

print(commonElements(ar1,ar2,ar3)) 
print(commonElements(ar1,ar2,ar3))