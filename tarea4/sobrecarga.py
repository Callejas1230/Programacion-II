class Sobrecarga:
    def area(self, *args):
        if len(args) == 1:  # Área de un círculo
            radio = args[0]
            return 3.141592653589793 * radio * radio
        
        elif len(args) == 2:  
            if isinstance(args[1], float):  # Área de un pentágono
                lado, apotema = args
                return (5 * lado * apotema) / 2
            else:  # Área de un rectángulo
                base, altura = args
                return base * altura
        
        elif len(args) == 3:  # Área de un trapecio
            base1, base2, altura = args
            return ((base1 + base2) / 2) * altura
        
        elif len(args) == 2 and isinstance(args[0], float) and isinstance(args[1], float):  # Área de un triángulo
            cateto1, cateto2 = args
            return (cateto1 * cateto2) / 2

    @staticmethod
    def main():
        s = Sobrecarga()
        print("Círculo:", s.area(5))  # Círculo
        print("Rectángulo:", s.area(2, 3))  # Rectángulo
        print("Triángulo:", s.area(3.0, 4.0))  # Triángulo
        print("Trapecio:", s.area(1, 2, 4))  # Trapecio
        print("Pentágono:", s.area(10.0, 5.0))  # Pentágono

# Llamada al método main
if __name__ == "__main__":
    Sobrecarga.main()
