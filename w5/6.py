# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

text = "Random text,idk:what.to.do"

pattern = "[ | , | .]"

res = re.sub(pattern, ":" , text)

print(res)