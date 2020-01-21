import pika
import json
from telebot import TeleBot


bot = TeleBot('1020375982:AAHmAOlDGxUEyqVNvWKaiBrk-2vPrHrKbGU')
CHAT_ID = 393055184


def callback(ch, method, properties, body):
    data = json.loads(body)
    bot.send_message(CHAT_ID, f"New {data['type']} added: {data['name']}")


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='127.0.0.1'
    ))
channel = connection.channel()

channel.queue_declare(queue='objects')

channel.basic_consume(
    queue="objects", on_message_callback=callback
)


if __name__ == "__main__":
    channel.start_consuming()

