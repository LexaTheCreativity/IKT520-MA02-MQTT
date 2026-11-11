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
    publish_message(publisher, "CyberSec/IKT520", "Hello there" ,1)

    time.sleep(2)

    subscriber.disconnect()
    subscriber.loop_stop()

if __name__ == "__main__":
    main()