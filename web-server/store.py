import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text)) #es un string en forma de una lista de diccionarios
    #convertiremos el string en una lista
    categories = r.json() #funcion esclusiva de requests que hace el trabajo
    for category in categories:
        print(category['name'])