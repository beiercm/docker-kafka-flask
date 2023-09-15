from confluent_kafka import Consumer

config = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'local_test',
    'auto.offset.reset': 'smallest'
}

consumer = Consumer(config)

topic = ["test_topic"]

consumer.subscribe(topic)

print("Consumer initialized")

while True:
    msg = consumer.poll(timeout=1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    key = msg.key()
    val = msg.value()
    offset = msg.offset()

    print(f"offset: {offset}, key: {key}, val: {val}")