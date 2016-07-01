import re

def file_name_regex(base_name):
    base_name = base_name.strip()
    print(base_name)
    return re.findall('^[A-Z]+\s[A-Z]+-[0-9]+', base_name)

print(file_name_regex(r'T BH-652 B3 PC'))