import java.util.Arrays;
import java.util.HashSet;

public class SetCase {
    public static void main(String[] args) {
        HashSet<String> set_array = new HashSet<>(Arrays.asList("H", "E", "L", "L", "O"));

        SetCase setcase = new SetCase();
        setcase.print_set(set_array);
    }

    public void print_set(HashSet<String> a) {
        System.out.println(a);
    }
}
