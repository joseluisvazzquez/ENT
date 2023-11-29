public class BuscadorNumero {
    public static void main(String[] args) {
        int[] numeros = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int numeroBuscado = 7;

        int indiceEncontrado = buscarNumero(numeros, numeroBuscado);

        if (indiceEncontrado >= 0) {
            System.out.println("Número encontrado en la posición: " + indiceEncontrado);
        } else {
            System.out.println("Número no encontrado.");
        }
    }

    public static int buscarNumero(int[] sort, int numeroBuscado) {
        int bajo = 0;
        int alto = sort.length - 1;

        while (bajo <= alto) {
            int medio = (bajo + alto) / 2;

            if (numeroBuscado < sort[medio]) {
                alto = medio - 1;
            } else if (numeroBuscado > sort[medio]) {
                bajo = medio + 1;
            } else {
                return medio;
            }
        }

        return -1; // Número no encontrado
    }
}
