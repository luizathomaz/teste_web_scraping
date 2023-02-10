import requests
from bs4 import BeautifulSoup
import json

url = 'http://books.toscrape.com/catalogue/category/books/childrens_11/page-1.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
#print(type(soup))
#print(soup)

nome = []
preco = []
estrela = []
stock = []

precos = soup.findAll('p', attrs={'class': 'price_color'})
for p in precos:
    preco.append(p.text)
#print(preco)

for n in soup.findAll('img', attrs={'class': 'thumbnail'}):
    nome.append(n['alt'])
#print(nome)

stocks = soup.findAll('p', attrs={'class': 'instock availability'})
for s in stocks:
    stock.append(s.text.strip())
#print(stock)

estrelateste = []
for e in soup.findAll('p', attrs={'class': 'star-rating'}):
    estrelateste.append(e['class'])
for v in estrelateste:
    estrela.append(v[1])
#print(estrela)

#formato: 
livrosteste = [
    [{'index': 1,
    'nome': 'nome do livro',
    'preco': 'preco do livro',
    'disponivel': 'in stock',
    'estrela': 'estrelas do livro'}],
    [{'index': 2,
    'nome': 'nome do livro',
    'preco': 'preco do livro',
    'disponivel': 'in stock',
    'estrela': 'estrelas do livro'}]
]


livros = []
for e in range(0, len(nome)):
    livros.append(
        {'index': e+1,
        'nome': nome[e],
        'preco': preco[e],
        'disponibilidade': stock[e],
        'estrelas': estrela[e]}
    )

publicacoes = {'livros': livros}
with open('json_publicacoes.json', 'w', encoding='utf8') as outfile:
    json.dump(publicacoes, outfile, indent=4, ensure_ascii=False)

