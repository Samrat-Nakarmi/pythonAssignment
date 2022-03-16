import re

# #1
# pwd = input("Enter your password: ")
# reg = re.search('^[a-z][A-Z]\w*\d[A-Z]$', pwd)
#
# if len(pwd)>=8 and reg:
#     print("Valid")
# else:
#     print("Not strong enough")

#2

list = [input(f'{i}=> ') for i in range(int(input('length =')))]
join = ','.join(list[:-1]) + ' and ' + list[-1]
print(join)