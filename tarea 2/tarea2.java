/*import java.awt.Color;
import java.awt.BasicStroke;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;

public class Punto {
    public float x;
    public float y;

    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public float[] coord_cartesianas() {
        return new float[]{x, y};
    }

    public float[] coord_polares() {
        float r = (float) Math.sqrt(x * x + y * y);
        float theta = (float) Math.atan2(y, x);
        return new float[]{r, theta};
    }

    @Override
    public String toString() {
        return "Punto{" + "x=" + x + ", y=" + y + '}';
    }
}
//LINEA
class Linea extends JPanel {

    private Punto punto1;
    private Punto punto2;

    public Linea(Punto punto1, Punto punto2) {
        this.punto1 = punto1;
        this.punto2 = punto2;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        g2.setColor(Color.BLUE);
        g2.setStroke(new BasicStroke(2));

        g2.draw(new Line2D.Double(punto1.x * 100, punto1.y * 100, punto2.x * 100, punto2.y * 100));
    }

    public static void main(String[] args) {
        Punto punto1 = new Punto(3, 1);
        Punto punto2 = new Punto(1, 5);

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new Linea(punto1, punto2));
        frame.setSize(400, 400);
        frame.setVisible(true);

//------------------------------------------------------
//CIRCUNFERENCIA

public class Circunferencia extends JPanel {

    private Punto centro;
    private float radio;

    public Circunferencia(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        g2.setColor(Color.RED);
        g2.setStroke(new BasicStroke(2));

        double x = centro.x * 100 - radio * 100;
        double y = centro.y * 100 - radio * 100;
        double width = radio * 200;
        double height = radio * 200;

        g2.draw(new Ellipse2D.Double(x, y, width, height));
    }

    public static void main(String[] args) {
        Punto centro = new Punto(2, 2);
        float radio = 1.5f; 

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new Circunferencia(centro, radio));
        frame.setSize(400, 400);
        frame.setVisible(true);
    }
}
