price = 3.1415    
price1 = 3.14151231    

# print(f"{price:10}")
# print(f"{price1:10}")
# print(f"{price:<10}")# left justified
# print(f"{price1:>10}")# right justified

price = 1342
# print(f"{price:010}")#should have 10 digits if not then add 0 to front
# print(f"{price:<010}")#should have 10 digits if not then add 0 to back

# print(f"{price:^10}")# centered
# print(f"{price1:^10}")# centered


price = -3123
price1 = 3123
# print(f"{price:+}")# specifies plus or minues
# print(f"{price1:+}")# specifies plus or minues

print(f"{price1:,}")# adds , for thousands

price = -3123

print(f"{price1:,.2f}")# adds , for thousands