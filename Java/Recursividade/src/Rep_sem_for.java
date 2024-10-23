public class Rep_sem_for {
    public static void main(String[] args) {
        int resultado = calc_fat(5);
        System.out.println(resultado);
    }
    public static int calc_fat(int n ){
        if(n == 0 || n == 1) {
            return 1;
        }
        else{
            return n * calc_fat(n-1);
        }
    }
}
