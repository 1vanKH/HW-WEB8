import json
from Task1.models import Author, Quote



def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_authors():
    authors_data = load_data_from_json('C:/Users/Savch/Documents/GitHub/HW-WEB8/hw-web8/Task1/authors.json')
    for author_data in authors_data:
        author = Author(
            fullname=author_data['fullname'],
            born_date=author_data['born_date'],
            born_location=author_data['born_location'],
            description=author_data['description']
        )
        author.save()

def load_quotes():
    quotes_data = load_data_from_json('C:/Users/Savch/Documents/GitHub/HW-WEB8/hw-web8/Task1/qoutes.json')
    for quote_data in quotes_data:
        quote = Quote(
            author=quote_data['author'],
            text=quote_data['quote'],
            tags=quote_data['tags']
        )
        quote.save()

if __name__ == '__main__':
    load_authors()
    load_quotes()
    print('Дані завантажено.')
