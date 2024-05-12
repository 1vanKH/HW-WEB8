from mongoengine import connect
from Task1.models import Quote

from mongoengine import connect
from Task1.models import Quote

def search_quotes(criteria):
    if criteria.startswith("name:"):
        author_name = criteria.split(":", 1)[1].strip()
        quotes = Quote.objects(author=author_name)
    elif criteria.startswith("tag:"):
        tag = criteria.split(":", 1)[1].strip()
        quotes = Quote.objects(tags__icontains=tag)
    elif criteria.startswith("tags:"):
        tags = criteria.split(":", 1)[1].strip().split(",")
        quotes = Quote.objects(tags__in=tags)
    else:
        print("Invalid search criteria. Please use 'name:', 'tag:' or 'tags:'")
        return

    for quote in quotes:
        print(f"Author: {quote.author}")
        print(f"Quote: {quote.text}")
        print(f"Tags: {', '.join(quote.tags)}")
        print()

if __name__ == "__main__":
    connect(host='mongodb+srv://goitlearn:41142058van@cluster0.hq9wumc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

    while True:
        command = input("Enter search criteria (name:<author_name>, tag:<tag>, tags:<tag1>,<tag2>,...): ")
        if command.lower() == "exit":
            break
        search_quotes(command)

