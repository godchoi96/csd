public class StringStructure {
    public static void main(String[] args) {
        String a1 = "Happy Java!";
        String a2 = new String("Happy Java!");

        StringStructure stringStructure = new StringStructure();
        stringStructure.print_String(a1);
        stringStructure.print_String(a2);
    }

    public void print_String(String a) {
        System.out.println(a);
    }
}
