public class StringStructureOther {
    public static void main(String[] args) {
        String a1 = "Happy Java!";
        String a2 = new String("Happy Java!");

        StringStructureOther stringStructureOther = new StringStructureOther();
        stringStructureOther.check_string(a1, a2);
    }

    public void check_string(String a, String b) {
        System.out.println(a.equals(b));
        System.out.println(a == b);
    }
}
