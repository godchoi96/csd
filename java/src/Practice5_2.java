class Calculator3 {
    Integer value;
    Calculator3() {
        this.value = 0;
    }
    void add(int val) {
        this.value += val;
    }
    public Integer getValue() {
        return this.value;
    }
}

public class Practice5_2 {
    public void main(String[] args) {
        Calculator3 cal = new Calculator3();
        cal.add(3);
        System.out.println(cal.getValue());
    }
}
