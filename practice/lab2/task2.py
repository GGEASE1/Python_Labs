import re

text = input()

pattern = r'[A-Za-z0-9+_#-]+@[A-Za-z0-9.-]+\.[A-Za-z]+'

result = re.findall(pattern, text)

for email in result:
    print(email)