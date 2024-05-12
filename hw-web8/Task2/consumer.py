import pika
from mongoengine import connect
from models import Contact

credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='test', exchange_type='direct')
channel.queue_declare(queue='test_queue', durable=True)
channel.queue_bind(exchange='test', queue='test_queue')

connect(db='test', host='mongodb+srv://goitlearn:41142058van@cluster0.hq9wumc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

def send_email(contact_id):
    print(f'Email було відправлено контакту з ID: {contact_id}')


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects.get(id=contact_id)
    contact.email_sent = True
    contact.save()
    send_email(contact_id)



channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print('Чекаю на повідомлення з черги...')
channel.start_consuming()
