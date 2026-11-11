import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
KEEPALIVE = 60

# MQTT message received from Broker
def on_message(client, userdata, message):
    print(f"Message received on {message.topic}, {message.payload.decode()}, (QoS={message.qos})")

# Define the on_connect callback (runs when the CONNACK arrives)
def on_connect(client, userdata, flags, reason_code, properties):
    print("CONNACK received...")
    print(f"    session_present = {flags.session_present}")
    print(f"    reason_code     = {reason_code} (value={reason_code.value})")
    print(f"    properties      = {properties}")


# Check SUBACK reply sent from Broker
def on_subscribe(client, userdata, msg_id, reason_code_list, properties):
    print("SUBACK received...")
    print("    msg_id = ", msg_id)
    if reason_code_list[0].is_failure:
        print(f"Broker rejected subscription, failure = {reason_code_list[0].value}")
    else:
        print(f"Broker accepted subscription, granted QoS = {reason_code_list[0].value}")

# Identifies which message was received by Broker
def on_publish(client, userdata, msg_id, reason_code, properties):
    print(f"Broker received message with msg_id={msg_id} ")

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


#Connect the publisher to Broker
def connect_publisher(publisher):
    publisher.on_connect = on_connect
    publisher.connect(BROKER, PORT, KEEPALIVE)
    publisher.loop_start()
    time.sleep(2)
    publisher.loop_stop()
    publisher.disconnect()


# Connect the subscriber to the Broker
def connect_subscriber(subscriber, topic, qos):
    subscriber.on_connect = on_connect
    subscriber.on_subscribe = on_subscribe
    subscriber.on_message = on_message

    subscriber.connect(BROKER, PORT, KEEPALIVE)
    subscriber.loop_start()
    time.sleep(2)

    result, msg_id = subscriber.subscribe(topic, qos)
    print(f"SUBSCRIBE sent: topic={topic}, qos={qos}, msg_id={msg_id}")
    time.sleep(2)

# Send out message
def publish_message(publisher, topic, msg, qos):
    publisher.on_connect = on_connect
    publisher.on_publish = on_publish

    publisher.connect(BROKER, PORT, KEEPALIVE)
    publisher.loop_start()
    time.sleep(2)

    msg_info = publisher.publish(topic, msg, qos)
    print(f"PUBLISH sent: topic={topic}, message={msg}, qos={qos}")
    msg_info.wait_for_publish()

    time.sleep(2)
    publisher.disconnect()
    publisher.loop_stop()