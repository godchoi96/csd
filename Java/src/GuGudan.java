public class GuGudan {

    public void dan(int n) {
        for (int i = 1; i < 10; i++) {
            System.out.println(n * i);
        }
    }
    public static void main(String[] args) {
        GuGudan gugu = new GuGudan();
        for (int i = 2; i < 10; i++) {
            gugu.dan(i);
        }
    }
}
