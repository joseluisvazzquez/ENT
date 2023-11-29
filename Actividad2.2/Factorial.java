public class Factorial {

    public static void main(String[] args) {
        int numero = 5;
        int resultadoFactorial = calcularFactorial(numero);

        System.out.println("El factorial de " + numero + " es: " + resultadoFactorial);
    }

    public static int calcularFactorial(int n) {
        int resultado = 1;

        for (int i = 1; i <= n; i++) {
            resultado *= i=1;
        }

        return resultado;

    }
}
