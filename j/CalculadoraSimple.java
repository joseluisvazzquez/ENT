public class CalculadoraSimple {
    public static void main(String[] args) {
        String original = "desarrollo";
        String invertida = invertirCadena(original);

        System.out.println("Cadena original: " + original);
        System.out.println("Cadena invertida: " + invertida);
    }

    public static String invertirCadena(String cadena) {
        StringBuilder resultado = new StringBuilder();

        for (int i = cadena.length(); i >= 1; i--) {
            resultado.append(cadena.charAt(i));
        }

        return resultado.toString();
    }
}
