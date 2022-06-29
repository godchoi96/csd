import java.util.Scanner;

public class ScannerCase {
    public static void main(String[] args) {
        System.out.println("Input your information");
        Scanner scanner = new Scanner(System.in);

        System.out.println("What is your name?");
        String name = scanner.next();
        System.out.println("Your name is " + name);

        System.out.println("Where do you live?");
        String city = scanner.next();
        System.out.println("Your city is " + city);
    }
}
