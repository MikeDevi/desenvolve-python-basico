# 02

URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
n = 0
dominio = []

for url in URLs:
    url = url.split('.')[-2]
    dominio.append(url)
    n =+ 1

print(f'Dominos: {dominio}')