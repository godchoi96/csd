interface Language {
    String getCode();
}

class Programming {
    String name;

    void setName(String name) {
        this.name = name;
    }
}

class Java extends Programming implements Language {
    public String getCode() {
        return "Java";
    }
}

class Python extends Programming implements Language {
    public String getCode() {
        return "Python";
    }
}

class Coder {
    void coding(Language language) {
        System.out.println("coding " + language.getCode());
    }
}

public class InterfaceCase {
    public static void main(String[] args) {
        Coder coder = new Coder();
        Java java = new Java();
        Python python = new Python();
        coder.coding(java);
        coder.coding(python);
    }
}
