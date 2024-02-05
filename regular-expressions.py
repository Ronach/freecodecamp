# re = regular expressions
import re

# with open("pyproject.toml", "rb") as f:
fhand = open('romeo.txt')
for line in fhand:
    # rstrip() right strip et lstrip() left strip. strip() agit à gauche et à droite.
    line = line.rstrip()
    if re.search('^oh', line):
        print(line)
g