from flask import Flask, request
from confluent_kafka import Producer
import socket

app = Flask(__name__)

config = {'bootstrap.servers': 'kafka:9092',
        'client.id': socket.gethostname()}

producer = Producer(config)
topic = "test_topic"

@app.route('/')
def hello():
    return 'Hello, World!'

@app.post('/addData')
def add_data():    
    key = request.json['key']
    value = request.json['value']
    producer.produce(topic, value, key)
    return 'info_added', 200