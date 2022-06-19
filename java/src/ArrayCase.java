public class ArrayCase {
    public static void main(String[] args) {
        int [] nums_array = {1, 2, 3, 4, 5};

        ArrayCase arrayCase = new ArrayCase();
        arrayCase.print_array(nums_array);

    }
    public void print_array(int [] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
    }
}
