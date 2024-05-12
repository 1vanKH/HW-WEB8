import pika
from mongoengine import connect
from faker import Faker
from models import Contact

credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='test', exchange_type='direct')
channel.queue_declare(queue='test_queue', durable=True)
channel.queue_bind(exchange='test', queue='test_queue')


connect(db='test', host='mongodb+srv://goitlearn:41142058van@cluster0.hq9wumc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


def generate_fake_contacts(num_contacts):
    fake = Faker()
    for _ in range(num_contacts):
        name = fake.name()
        email = fake.email()
        contact = Contact(full_name=name, email=email)
        contact.save()
        channel.basic_publish(exchange='', routing_key='test_queue', body=str(contact.id))


if __name__ == '__main__':
    num_contacts = 15  
    generate_fake_contacts(num_contacts)
    print(f'{num_contacts} фейкових контактів було створено та відправлено у чергу.')
