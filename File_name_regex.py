import re

file_name = 'PP BH-649 B3 PB.txt'.strip()
t_name = 'T BH-649 B3 PB.txt'.strip()

print(re.findall('^[A-Z]+\s[A-Z]+-[0-9]+', file_name))
print(re.findall('^[A-Z]+\s[A-Z]+-[0-9]+', t_name))