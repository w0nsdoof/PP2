# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

pattern = ".[A-Z][a-z]+"

text = "KOGDA nibud dosti_gny Globala" # Globala

res = re.search(pattern, text)

print(res)