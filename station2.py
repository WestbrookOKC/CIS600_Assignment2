import time
import random
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import datetime
# Set up MQTT client
client = AWSIoTMQTTClient("device")
client.configureEndpoint("a1ezbd0l3p8fzz-ats.iot.us-east-2.amazonaws.com", 8883)
client.configureCredentials("./root-CA.crt", "./sensor_station1.private.key", "./sensor_station1.cert.pem")

# Connect to AWS IoT
client.connect()

# Publish virtual sensor data to MQTT topic
while True:
    # temperature = random.randint(10, 30)
    # humidity = random.randint(40, 60)
    # payload = '{"temperature":' + str(temperature) + ',"humidity":' + str(humidity) + '}'
    timestamp = str(datetime.datetime.now())
    payload = {
        "station_id": "station-2",
        "temperature": random.uniform(-50, 50),
        "humidity": random.uniform(0, 100),
        "co2": random.uniform(300, 2000),
        "rain_height": random.uniform(0, 50),
        "wind_direction": random.uniform(0, 360),
        "wind_intensity": random.uniform(0, 100),
        'timestamp': timestamp
    }
    #client.publish("my/topic", json.dumps(payload), 1)
    client.publish("device/1/data", json.dumps(payload), 1)
    time.sleep(5)
