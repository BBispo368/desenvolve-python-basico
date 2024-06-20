URLs = ["www.google.com&quot", "www.gmail.com&quot", "www.github.com&quot", "www.reddit.com&quot", "www.yahoo.com&quot"]
dominio = []

for i in range(len(URLs)):
    dominio.append(URLs[i][4:-9])

print(URLs)
print(dominio)