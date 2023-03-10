# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

pattern = "a.*b$"

text = ["acd" , "azcb" , "abb" , "swsdwasdwdsb"]# acb azcb abb asdwdsb

for s in text:
    print(re.search(pattern, s))