
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class AL {

    public static void main(String[] args) {
        String nrElementos = JOptionPane.showInputDialog("Quantos numeros a lista vai ter");

        int nElementos = Integer.valueOf(nrElementos);

        ArrayList<Integer> lista = new ArrayList<Integer>();

        for (int i = 0; i < nElementos; i++) {
            String valor = JOptionPane.showInputDialog("Informe o valor " + i);
            lista.add(Integer.valueOf(valor));
        }
        System.out.println(lista);

        int soma = 0;
        for (int i = 0; i < lista.size(); i++) {
            soma = soma + lista.get(i);
        }
        System.out.println(soma);

        int soma_par = 0;
        for ( )

    }
}
