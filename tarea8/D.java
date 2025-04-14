package tarea8;

class D extends A {
    int y, zB;

    public D(int x, int y, int zA, int zB) {
        super(x, zA);
        this.y = y;
        this.zB = zB;
    }

    public void incrementaXYZ() {
        x++;
        y++;
        z++;
    }
}