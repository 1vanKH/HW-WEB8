from mongoengine import Document, StringField, ListField, connect


connect(host='mongodb+srv://goitlearn:41142058van@cluster0.hq9wumc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)

class Quote(Document):
    text = StringField(required=True)
    author = StringField(required=True)
    tags = ListField(StringField())