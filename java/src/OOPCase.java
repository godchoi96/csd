class Calculator {
    int result = 0;
    int add(int num) {
        result += num;
        return result;
    }
    int sub(int num) {
        result -= num;
        return result;
    }
    int mul(int num) {
        result *= num;
        return result;
    }
    int div(int num) {
        result /= num;
        return result;
    }
}

public class OOPCase {
    public static void main(String[] args) {
        Calculator calculator1 = new Calculator();
        Calculator calculator2 = new Calculator();

        System.out.println(calculator1.add(3));
        System.out.println(calculator1.add(7));
        System.out.println(calculator2.add(3));
        System.out.println(calculator2.add(7));
    }
}
