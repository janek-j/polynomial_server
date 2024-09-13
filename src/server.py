import socket
import polynomial
import visualize_poly


class PolynomialServer(polynomial.Polynomial):
    def __init__(self, port: int, coeffs):
        self.port = port
        self.address = 'localhost'

    def get_port(self):
        return self.port

    def get_address(self):
        return self.address

    def create_server(self):
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = self.get_address()
        port = self.get_port()
        server_address = (address, port)

        print(f"Starting server on {address}:{port}")

        tcp_socket.bind(server_address)
        tcp_socket.listen(2)

        while True:
            print("Waiting for the connection.\n")
            client_socket, client_address = tcp_socket.accept()
            try:
                print(f"Connection from client: {client_address}.")
                while True:
                    data = client_socket.recv(1024)
                    if data:
                        data_str = data.decode().strip()
                        coeffs = [float(c) for c in data_str.split()]

                        print(f"Received coefficients: {coeffs}\n")

                        # Tworzenie obiektu Polynomial
                        poly = polynomial.Polynomial(coeffs)
                        print(f"Constructed Polynomial: {poly}\n")

                        # Wizualizacja wielomianu
                        visualization = visualize_poly.VisualizePoly(coeffs)
                        visualization.plot(title="Polynomial Visualization")

                        response = str(poly).encode()
                        client_socket.sendall(response)
                    else:
                        print(f"Client {client_address} disconnected.")
                        break
            finally:
                client_socket.close()
