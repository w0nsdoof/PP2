# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

pattern = "[a-z]+_"

res = re.search(pattern, input())

print(res)