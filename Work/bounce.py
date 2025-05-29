# bounce.py
#
# Exercise 1.5
i = 1
h = 100
hlis = []

while i < 11:
    h = round(h * 3 / 5, 4)
    print(i, f'{h:>.4f}')
    hlis.append(h)
    i += 1

adj = max(hlis)
for x in hlis:
    k = int(round(80*x/adj, 0))
    print('/'*k)
