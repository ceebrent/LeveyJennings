import re

def file_name_regex(base_name):
    base_name = base_name.strip()
    return re.findall('^[A-Z]+\s*[A-Z]+-[0-9]+', base_name)[0]

base_name = r'T BH-619 B3 PA & PE'

print(file_name_regex(base_name))