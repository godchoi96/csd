public class MethodCase {
    int c;

    void cTest() {
        this.c++;
    }
    void say_ver2() {
        System.out.println("Hi");
    }

    void sum_ver2(int a, int b) {
        System.out.println(a + " + " + b + " is " + (a + b));
    }

    String say() {
        return "Hi";
    }

    int sum(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int a = 3;
        int b = 4;

        MethodCase methodCase = new MethodCase();
        System.out.println(methodCase.sum(a, b));
        System.out.println(methodCase.say());
        methodCase.sum_ver2(a, b);
        methodCase.say_ver2();
        methodCase.c = 30;
        methodCase.cTest();
        System.out.println(methodCase.c);
    }
}

