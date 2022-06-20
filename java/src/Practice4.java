public class Practice4 {
    public static void main(String[] args) {
        int[] marks = {70, 60, 55, 75, 95, 90, 80, 80, 85, 100};

        Practice4 practice4 = new Practice4();
        practice4.print_2();
        practice4.print_3();
        practice4.print_4();
        practice4.print_5(marks);
    }
    public void print_2() {
        int i = 1;
        int sum = 0;
        while (i <= 1000) {
            if (i % 3 == 0) {
                sum += i;
            }
            i++;
        }
        System.out.println(sum);
    }
    public void print_3() {
        for (int i = 1; i < 6; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print('*');
            }
            System.out.println("");
        }
    }
    public void print_4() {
        for (int i = 0; i <= 100; ++i) {
            System.out.print(i + " ");
        }
        System.out.println("");
    }
    public void print_5(int[] a) {
        double sum = 0;
        for (int score: a) {
            sum += score;
        }
        System.out.println(sum / 10);
    }
}
