from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(100):
    if e % 5 == 0:
        data = {'id':e, 'description':"UHasselt"}
    elif e % 2 == 0:   
        data = {'id':e, 'description':"UCLL"}
    else: 
        data = {'id':e, 'description':"Hogeschool PXL"}
    producer.send('schools', value=data)
    print(e)
    print(f"Sending data : {data}")
    sleep(15)
