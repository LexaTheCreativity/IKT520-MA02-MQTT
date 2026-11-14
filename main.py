# from clients import create_clients, connect_publisher, connect_subscriber, publish_message
from clients import *


def main():
    # Q1
    publisher, subscriber = create_clients()

    # Q2
    print("=== Q2: Publisher connect ===")
    connect_publisher(publisher)

    # Q3
    print("=== Q3: Subscriber connect ===")
    connect_subscriber(subscriber, "CyberSec/IKT520", 1)

    # Q4
    print("=== Q4: Publish message ===")
    publish_message(publisher, "CyberSec/IKT520", "Hello there", 1)

    time.sleep(2)

    # Q5
    print("=== Q5: Publish message ===")
    # Defining two wildcard topics
    wildcard_single = "CyberSec/+/Temp"
    wildcard_multi  = "CyberSec/IKT520/#"

    # Using the subscriber to make two subscriptions 
    subscriber.subscribe(wildcard_single, qos=1)
    subscriber.subscribe(wildcard_multi, qos=1)
    time.sleep(2)

    # Publishing several topics to test the wildcards
    publish_message(publisher, "CyberSec/IKT520/Temp", "Test 1", 1)
    publish_message(publisher, "CyberSec/Network/Temp", "Test 2", 1)
    publish_message(publisher, "CyberSec/IKT520/Multilevel1/level2/level3", "Test 3", 1)
    publish_message(publisher, "CyberSec/Temp", "Test 4", 1)

    # Disconnect Q1-Q5 subscriber
    subscriber.disconnect()
    subscriber.loop_stop()
    time.sleep(1)

    # Q6: Clean Session = FALSE
    print("\n=== Q6: Clean Session = False ===")

    # 1. Create clients using create_clients() with clean_session=False
    clientPublisher, clientSubscriber = create_clients(clean_session=False)
    connect_subscriber(clientSubscriber, "Sensor/Temp", qos=1)

    # 2. Disconnect subscriber
    print("\n--- Disconnecting Subscriber for Q6 ---")
    time.sleep(2)
    clientSubscriber.disconnect()
    clientSubscriber.loop_stop()

    # 3. Publish 20 messages while subscriber is offline
    print("\n--- Publishing 20 messages while subscriber is offline ---")
    clientPublisher.connect(BROKER, PORT, KEEPALIVE)
    clientPublisher.loop_start()
    time.sleep(2)

    for i in range(1, 21):
        clientPublisher.publish("Sensor/Temp", "Temp reading " + str(i), qos=1)
        time.sleep(0.05)

    time.sleep(2)
    clientPublisher.disconnect()
    clientPublisher.loop_stop()

    # 4. Reconnect subscriber
    print("\n--- Reconnecting Subscriber ---")
    clientSubscriber.connect(BROKER, PORT, KEEPALIVE)
    clientSubscriber.loop_start()
    time.sleep(5)  # Wait for broker response
    clientSubscriber.disconnect()
    clientSubscriber.loop_stop()

    # Q7
    print("\n=== Q7: Clean Session = True ===")
    # 1. Create clients using create_clients() with clean_session=True
    clientPublisher, clientSubscriber = create_clients(clean_session=True)
    connect_subscriber(clientSubscriber, "Sensor/Temp", qos=1)

    # 2. Disconnect subscriber
    print("\n--- Disconnecting Subscriber for Q7 ---")
    time.sleep(2)
    clientSubscriber.disconnect()
    clientSubscriber.loop_stop()

    # 3. Publish 20 messages while subscriber is offline
    print("\n--- Publishing 20 messages while subscriber is offline ---")
    clientPublisher.connect(BROKER, PORT, KEEPALIVE)
    clientPublisher.loop_start()
    time.sleep(2)

    for i in range(1, 21):
        clientPublisher.publish("Sensor/Temp", "Temp reading " + str(i), qos=1)
        time.sleep(0.05)

    time.sleep(2)
    clientPublisher.disconnect()
    clientPublisher.loop_stop()

    # 4. Reconnect subscriber
    print("\n--- Reconnecting Subscriber ---")
    clientSubscriber.connect(BROKER, PORT, KEEPALIVE)
    clientSubscriber.loop_start()
    time.sleep(5)  # Wait for broker response
    clientSubscriber.disconnect()
    clientSubscriber.loop_stop()

    # Q8
    print("\n=== Q8: Clean Session = False&&qos=0 ===")
    # 1. Create clients using create_clients() with clean_session=False
    clientPublisher, clientSubscriber = create_clients(clean_session=False)
    connect_subscriber(clientSubscriber, "Sensor/Temp", qos=0)

    # 2. Disconnect subscriber
    print("\n--- Disconnecting Subscriber for Q8 ---")
    time.sleep(2)
    clientSubscriber.disconnect()
    clientSubscriber.loop_stop()

    # 3. Publish 20 messages while subscriber is offline
    print("\n--- Publishing 20 messages while subscriber is offline ---")
    clientPublisher.connect(BROKER, PORT, KEEPALIVE)
    clientPublisher.loop_start()
    time.sleep(2) 

    for i in range(1, 21):
        #publisher qos=2
        clientPublisher.publish("Sensor/Temp", "Temp reading " + str(i), qos=2)
        time.sleep(0.05)

    time.sleep(2)
    clientPublisher.disconnect()
    clientPublisher.loop_stop()

    # 4. Reconnect subscriber
    print("\n--- Reconnecting Subscriber ---")
    clientSubscriber.connect(BROKER, PORT, KEEPALIVE)
    clientSubscriber.loop_start()
    time.sleep(5)  # Wait for broker response
    clientSubscriber.disconnect()
    clientSubscriber.loop_stop()


if __name__ == "__main__":
    main()
