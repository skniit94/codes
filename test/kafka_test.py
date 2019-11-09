from kafka import KafkaConsumer

from_topic = "gia_user_messages"
consumer = KafkaConsumer(from_topic, bootstrap_servers="kafka01.prod.goibibo.com:9092", auto_offset_reset="latest")
count = 0
for msg in consumer:
    count = count + 1
    print(str(count) + "\t" + str(msg.key) + "\t" + str(msg.value))
consumer.close()