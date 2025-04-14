package tarea8;

public class Main {
    public static void main(String[] args) {
        int x = 5, zA = 20, y = 10, zB = 10;

        D d = new D(x, y, zA, zB);

        System.out.println("x = " + d.x + ", y = " + d.y + ", z(A) = " + d.z + ", z(B) = " + d.zB);

        d.incrementaXYZ();

        System.out.println("x = " + d.x + ", y = " + d.y + ", z(A) = " + d.z + ", z(B) = " + d.zB);
    }
}