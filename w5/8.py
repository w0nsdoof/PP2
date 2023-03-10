import re

def split_capital(match):
    return " " + match.group(1) + match.group(2) 

text = "RandomTextNeedToSpaceBetweenCapitalLetters"
pattern = "([A-Z])([a-z])" # bukvi_bukvi (1)(2)(3)

res = re.sub(pattern, split_capital, text)

res = res[1:]

res = re.split("\s" , res)

print(res)

