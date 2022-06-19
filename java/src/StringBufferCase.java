public class StringBufferCase {
    public static void main(String[] args) {
        StringBuffer a1 = new StringBuffer();
        a1.append("Hi");
        a1.append(" ");
        a1.append("my name is CSD");

        StringBufferCase stringBufferCase = new StringBufferCase();
        stringBufferCase.append_string(a1);
    }

    public void append_string(StringBuffer a) {
        System.out.println(a);
    }
}
