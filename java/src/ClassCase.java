class Introduce {
    String name;
    public void introduceName(String name) {
        this.name = name;
    }
}

public class ClassCase {
    public static void main(String[] args) {
        Introduce introduce = new Introduce();
        introduce.introduceName("ChoiSeongdae");
        System.out.println(introduce.name);
    }
}
