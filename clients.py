import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
KEEPALIVE = 60

# Define the on_connect callback (runs when the CONNACK arrives)
def on_connect(client, userdata, flags, reason_code, properties):
    print("CONNACK received...")
    print(f"    session_present = {flags.session_present}")
    print(f"    reason_code     = {reason_code} (value={reason_code.value})")
    print(f"    properties      = {properties}")


# Q1: create the two clients
def create_clients():
    publisher = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
        client_id="IKT520_publisher"
    )
    subscriber = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
        client_id="IKT520_subscriber"
    )
    return publisher, subscriber


#Connect the publiosher to broker
def connect_publisher(publisher):
    publisher.on_connect = on_connect
    publisher.connect(BROKER, PORT, KEEPALIVE)
    publisher.loop_start()
    time.sleep(2)
    publisher.loop_stop()
    publisher.disconnect()