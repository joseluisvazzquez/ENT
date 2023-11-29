public class CadenaInvertida {
    public static void main(String[] args) {
        String original = "desarrollo";
        String invertida = invertirCadena(original);

        System.out.println("Cadena original: " + original);
        System.out.println("Cadena invertida: " + invertida);
    }

    public static String invertirCadena(String cadena) {
        StringBuilder resultado = new StringBuilder();

        for (int i = cadena.length()-1; i >= 0; i--) {
            resultado.append(cadena.charAt(i));
        }

        return resultado.toString();
    }
}
