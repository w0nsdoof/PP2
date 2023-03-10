# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

pattern = "a.{2,3}b"

res = re.search(pattern, input())

print(res)