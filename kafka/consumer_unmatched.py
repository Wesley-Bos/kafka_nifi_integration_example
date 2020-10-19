from kafka import KafkaConsumer

print("Connecting to consumer ...")
consumer = KafkaConsumer(
        'UHASSELT',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id='my-group')

for message in consumer:
 print(f"{message.value}")
