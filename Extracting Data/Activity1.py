import re 
file = open('regex_sum_2132824.txt')
read = file.read()
lst = list()
find = re.findall('[0-9]+',read)
for x in find:
    y = int(x)
    lst.append(y)
print(sum(lst))
