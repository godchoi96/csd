import java.util.ArrayList;

public class ListCase {
    public static void main(String[] args) {
        ArrayList randomNumber = new ArrayList();
        randomNumber.add("123");
        randomNumber.add("456");
        randomNumber.add("789");

        ArrayList arrayList = new ArrayList();
        arrayList.print_list(randomNumber);
    }
    public void print_list(ArrayList n) {
        System.out.println(n);
    }
}
