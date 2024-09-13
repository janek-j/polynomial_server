import client
def main():
    port = 8080
    address = 'localhost'
    my_client = client.PolynomialClient(port, address)
    my_client.create_client()

if __name__ == "__main__":
    main()
