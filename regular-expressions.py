# for regular expressions
import re

# with open("pyproject.toml", "rb") as f:
fhand = open('romeo.txt')
for line in fhand:
    line = line.rstrip()  # right strip et lstrip() retire à gauche. strip() retire au début et à la fin de la string
    if re.search('^oh', line):
        print(line)
