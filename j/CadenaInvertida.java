public class CadenaInvertida {
    public static void main(String[] args) {
        int a = 5;
        int b = 1;

        int suma = add(a, b);
        System.out.println("La suma de " + a + " y " + b + " es " + suma);

        int division = divide(a, b);
        System.out.println("La división de " + a + " por " + b + " es " + division);
    }

    public static int add(int x, int y) {
        return x + y;
    }

    public static int divide(int x, int y) {
            return x/y;
    }
    
}
