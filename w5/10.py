# Write a Python program to convert a given camel case string to snake case. # snake_case <- CamelCase

import re

def camel_cnvrt(match):
    return "_" + match.group(1).lower() + match.group(2)


text = "TheresSomeRandomTextSeperatedByThat"
pattern = "([A-Z])([a-z])" # bukvi_bukvi (1)(2)(3)

res = re.sub(pattern, camel_cnvrt, text)

print(res[1:])