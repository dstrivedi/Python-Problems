# Python 3.6, and beyond
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_incomes = {k:incomes[k] for k in sorted(incomes)}
print("sorted dictionary -> ", sorted_incomes)