class Updater {
    void update(Counter counter) {
        counter.count++;
    }
}

class Counter {
    int count = 0;
}

public class CallByValueCase {
    public static void main(String[] args) {
        Counter counter = new Counter();
        System.out.println("Before update: " + counter.count);
        Updater updater = new Updater();
        updater.update(counter);
        System.out.println("after update: " + counter.count);
    }
}
