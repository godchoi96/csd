public class TypeTransFinalCase {
    public static void main(String[] args) {
        String num = "123";
        int n = 123;
        final int none_change = 456;

        none_change = 456; // 실행 시, 이 부분 제거 필요.
        System.out.println(none_change);
        TypeTransFinalCase typeTrans = new TypeTransFinalCase();
        typeTrans.print_inttrans(num);
        typeTrans.print_stringtrans(n);
    }
    public void print_inttrans(String a) {
        int change_a = Integer.parseInt(a);
        System.out.println(change_a);
    }
    public void print_stringtrans(int a) {
        String change_a = Integer.toString(a);
        System.out.println(change_a);
    }
}
