import java.util.ArrayList;
import java.util.Arrays;

class PracCalculator {
    int value;

    PracCalculator() {
        this.value = 0;
    }

    void add(int val) {
        this.value += val;
    }

    int getValue() {
        return this.value;
    }

    boolean isOdd(int val) {
        if (val % 2 == 0) {
            return false;
        } else {
            return true;
        }
    }

    double avg(int[] val) {
        int sum = 0;
        for (int i = 0; i < val.length; i++) {
            sum += val[i];
        }
        return (sum / val.length);
    }

    double avg(ArrayList<Integer> val) {
        int sum = 0;
        for (int i = 0; i < val.size(); i++) {
            sum += val.get(i);
        }
        return (sum / val.size());
    }
}

class UpgradeCalculator extends PracCalculator {
    void minus(int val) {
        this.value -= val;
    }
}

class MaxLimitCalculator extends PracCalculator {
    void add(int val) {
        this.value += val;
        if (this.value >= 100) {
            this.value = 100;
        }
    }
}

public class Practice5 {
    public static void main(String[] args) {
        UpgradeCalculator cal = new UpgradeCalculator();
        cal.add(10);
        cal.minus(3);
        System.out.println(cal.getValue());

        MaxLimitCalculator cal2 = new MaxLimitCalculator();
        cal2.add(50);
        cal2.add(60);
        System.out.println(cal2.getValue());

        PracCalculator cal3 = new PracCalculator();
        System.out.println(cal3.isOdd(3));

        int[] data = {1, 3, 5, 7, 9};
        double result = cal3.avg(data);
        System.out.println(result);

        ArrayList<Integer> data2 = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9));
        double result2 = cal3.avg(data2);
        System.out.println(result2);

        ArrayList<Integer> a = new ArrayList<>(Arrays.asList(1, 2, 3));
        ArrayList<Integer> b = a;
        a.add(4);
        System.out.println(b.size());
    }
}