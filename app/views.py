from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup
import requests


# Create your views here.
def crawler(request, value):
    url = f"https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/{value}"
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, 'html.parser')
    for parse_tree in content.find_all('div', attrs={'class': 'verbete bs-component'}):
        result = parse_tree.contents[9]

    return render(request, "index.html", {"value": value , "result": result})
