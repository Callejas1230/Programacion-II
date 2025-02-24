//public class Circulo {
    //public float x;
    //public float y;
    //public Circulo(float x, float y) {
        //x = 0;
        //y = 0;
    //}
    //public float coord_cartesianas(){
        //return (x,y);
    //}
    //public float coord_polares(){
        //return 
    //}
    //public float toString(){
        
    //}//
    


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
    