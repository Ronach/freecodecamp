# on veut avoir chaque mot dans le texte et son nombre d'apparition

# with open("pyproject.toml", "rb") as f:
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()  # retourne une liste. Par défaut, sépare par les espaces. On peut préciser split(";") par exemple
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)
# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) ) est équivalent aux lignes ci-dessous
liste = list()
for key, val in counts.items():
    newtup = (val, key)
    liste.append(newtup)  # liste de tuples

print(liste)
liste = sorted(liste, reverse=True)  # reverse true pour aller du plus grand au plus petit selon la "val"
print(liste)

for val, key in liste[:]:
    print(key, val)


