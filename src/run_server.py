import polynomial
import visualize_poly
import server
import client

def main() -> None:
    print("Funkcja glowna\n")
    serv = server.PolynomialServer(8080, [])
    serv.create_server()

    return None

if __name__ == "__main__":
    main()