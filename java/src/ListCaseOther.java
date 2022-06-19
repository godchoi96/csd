import java.util.ArrayList;

public class ListCaseOther {
    public static void main(String[] args) {
        ArrayList<String> randomNumber = new ArrayList<>();
        randomNumber.add("123");
        randomNumber.add("456");
        randomNumber.add("789");

        ListCaseOther listCaseOther = new ListCaseOther();
        listCaseOther.print_list(randomNumber);
    }
    public void print_list(ArrayList<String> n) {
        System.out.println(n);
    }
}
