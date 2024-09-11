
import java.util.HashSet;

public class App {

    public static void main(String[] args) {
        HashSet<String> carro = new HashSet<String>();
        carro.add("Volvo");
        carro.add("BMW");
        carro.add("Ford");
        carro.add("Bmw");
        carro.add("Mazda");

        System.out.println(carro);
    }
}
