public class Insertion_sort {
    /*função que organiza o array usando insertion */
    void organizar(int lista[])
    {
        int tamanho = lista.length;
        for (int i = 1; i < tamanho; ++i) {
            int chave = lista[i];
            int j = i -1;
        /*move os elementos do array lista, que são maiores que o valor chave
         * para uma posição para frente da sua posição atual*/
        while (j >= 0 && lista[j] > chave){
            lista[j + 1] = lista[j];
            j = j - 1;
        }
        lista[j + 1] = chave;
        }
        
    }
    /*literalmente e uma função pra dar o print com cada valor em uma linha */
    static void printLista(int lista[])
    {
        int tamanho = lista.length;
        for (int i = 0; i < tamanho; ++i)
            System.out.println(lista[i] + " ");
            
        System.out.println();
    }

    public static void main(String args[]) 
    {
        /*variavel da lista */
        int lista[] = {12, 11, 13, 5, 6};

        /*o tempo inicial, a função para organizar a lista, tempo final */
        long tempoInicial = System.currentTimeMillis();
        Insertion_sort ob = new Insertion_sort();
        ob.organizar(lista);
        long tempoFinal = System.currentTimeMillis();

        /*o print de tudo */
        printLista(lista);
        System.out.println("Tempo de execução: " + (tempoFinal - tempoInicial) + "ms");
    }
}
