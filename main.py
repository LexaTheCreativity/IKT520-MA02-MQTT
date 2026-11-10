from clients import create_clients, connect_publisher


def main():
    # Q1
    publisher, subscriber = create_clients()

    # Q2
    print("=== Q2: Publisher connect ===")
    connect_publisher(publisher)


if __name__ == "__main__":
    main()