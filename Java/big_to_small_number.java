public class Main {
    public static void main(String[] args) {
        for (int i = 1000; i > 0; i--) {
            if (i % 5 == 0) {
                System.out.println();
            }
            System.out.print(i + "\t");
        }
    }
}
