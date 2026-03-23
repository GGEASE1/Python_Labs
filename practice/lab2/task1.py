import re

text = input()

pattern = r'\b20\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01]) (?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\b'

result = re.findall(pattern, text)

for x in result:
    print(x)