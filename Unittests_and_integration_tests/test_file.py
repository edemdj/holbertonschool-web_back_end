#!/usr/bin/env python3

from utils import get_json

url = "https://jsonplaceholder.typicode.com/todos/1"

data = get_json(url)
print(data)


url = "https://jsonplaceholder.typicode.com/todos/999999999"

try:
    data = get_json(url)
    print("Réponse reçue :", data)
except Exception as e:
    print("Une erreur s'est produite :", repr(e))
