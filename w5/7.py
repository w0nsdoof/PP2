# Write a python program to convert snake case string to camel case string. # snake_case -> CamelCase

import re

def camel_cnvrt(match):
    return match.group(1) + match.group(3).upper()


text = "Theres_some_random_text_seperated_by_that"
pattern = "([a-z])([_])([a-z])" # bukvi_bukvi (1)(2)(3)

res = re.sub(pattern, camel_cnvrt, text)
res = res[0].upper() + res[1:]

print(res)
