import java.util.*;

public class Practice3 {
    enum CoffeList {
        AMERICANO,
        ICED_AMERICANO,
        CAFE_LATTE
    };
    public static void main(String[] args) {
        int kor = 80, eng = 75, math = 55;
        int num2 = 13;
        StringBuffer hong = new StringBuffer("881120-1068234");
        String pin = "881120-1068234";
        String a = "a:b:c:d";
        ArrayList<Integer> myList6 = new ArrayList<>(Arrays.asList(1, 3, 5, 4, 2));
        ArrayList<String> myList7 = new ArrayList<>(Arrays.asList("Life", "is", "too", "short"));
        HashMap<String, Integer> grade = new HashMap<>();
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5));

        Practice3 practice3 = new Practice3();
        practice3.print_1(kor, eng, math);
        practice3.print_2(num2);
        practice3.print_3(hong);
        practice3.print_4(pin);
        practice3.print_5(a);
        practice3.print_6(myList6);
        practice3.print_7(myList7);
        practice3.print_8(grade);
        practice3.print_9(numbers);
        CoffeePrice(CoffeList.AMERICANO);
    }
    public void print_1(int a, int b, int c) {
        double avg;
        avg = (a + b + c) / 3;
        System.out.println(avg);
    }
    public void print_2(int a) {
        String result;
        if (a % 2 == 0) {
            result = "even number";
        } else {
            result = "odd number";
        }
        System.out.println(result);
    }
    public void print_3(StringBuffer a) {
        System.out.println("First is " + a.substring(0, 6));
        System.out.println("Last is " + a.substring(7, 14));
    }
    public void print_4(String a) {
        System.out.println(a.charAt(7));
    }
    public void print_5(String a) {
        a = a.replace(":", "#");
        System.out.println(a);
    }
    public void print_6(ArrayList a) {
        Collections.sort(a, Collections.reverseOrder());
        System.out.println(a);
    }
    public void print_7(ArrayList a) {
        System.out.println(String.join(" ", a));
    }
    public void print_8(HashMap<String, Integer> a) {
        a.put("A", 90);
        a.put("B", 80);
        a.put("C", 70);
        int result = a.remove("B");
        System.out.println(result);
        System.out.println(a);
    }
    public void print_9(ArrayList<Integer> a) {
        HashSet<ArrayList<Integer>> answer = new HashSet(a);
        System.out.println(answer);
    }
    static void CoffeePrice(CoffeList type) {
        HashMap<CoffeList, Integer> priceMap = new HashMap<>();
        priceMap.put(CoffeList.AMERICANO, 3000);
        priceMap.put(CoffeList.ICED_AMERICANO, 4000);
        priceMap.put(CoffeList.CAFE_LATTE, 5000);
        int price = priceMap.get(type);
        System.out.println(String.format("Price is %dwon.", price));
    }

}
