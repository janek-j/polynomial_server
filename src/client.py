import server
import socket
class PolynomialClient(server.PolynomialServer):
    def __init__(self, port: int, address = 'localhost'):
        super().__init__(port, address)

    def create_client(self):
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = (self.address, self.port)

        print(f"Connecting client to: {self.address}:{self.port}")

        try:
            tcp_socket.connect(server_address)
            print(f"Connected to server at {self.address}:{self.port}.\n")
            coeffs_input = input("Enter coefficients of the Polynomial (Separated by spaces): ")
            tcp_socket.sendall(coeffs_input.encode())

            response = tcp_socket.recv(1024)
            if response:
                print("Received polynomial from server:", response.decode())
        except ConnectionError as e:
            print("Error connecting to server ", e)
        finally:
            tcp_socket.close()
            print("Connection closed")

