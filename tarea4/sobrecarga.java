package tarea4;

public class Sobrecarga {
    double area(double radio){
        return Math.PI * radio * radio ;
    
    }    
    double area(double base,double altura){
        return base * altura;
    }
    double area(float cateto1,float cateto2){
        return (cateto1 * cateto2)/2;
    }
    float area(float base1, float base2, float altura){
        return ((base1 + base2)/2) * altura;
    }
    double area(float lado, double apotema){
        return (5 * lado * apotema)/2;
    }

    public static void main(String[] args){
        Sobrecarga S1circulo = new Sobrecarga();
        Sobrecarga S2rectanglo = new Sobrecarga();
        Sobrecarga S3triangulo = new Sobrecarga();
        Sobrecarga S4trapecio = new Sobrecarga();
        Sobrecarga S5pentagono = new Sobrecarga();
        System.out.println("Circulo: " + S1circulo.area(5));
        System.out.println("Rectangulo: " + S2rectanglo.area(2, 3));
        System.out.println("Triangulo: " + S3triangulo.area(3, 4));
        System.out.println("Trapecio: " + S4trapecio.area(1, 2, 4));
        System.out.println("Pentagono: " + S5pentagono.area(10, 5));
    }
}
