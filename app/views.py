from django.shortcuts import render
from django.shortcuts import HttpResponse
from bs4 import BeautifulSoup
import requests


# Create your views here.
def crawler(request, value):
    url = f"https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/{value}"
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.text, "html.parser")
    word = content.find(class_="verbete bs-component")
    new_cont = word.find_all('eu')
    return HttpResponse(new_cont)
