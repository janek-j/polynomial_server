import polynomial
import visualize_poly
import server

def main() -> None:
    print("Funkcja glowna\n")
    poly = visualize_poly.VisualizePoly([1])
    poly.plot()
    return None

if __name__ == "__main__":
    main()