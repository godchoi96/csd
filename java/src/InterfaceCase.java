interface FrameworkLanguage {
    void thisframework();
}

interface Language {
    String getCode();
}

class Programming {
    String name;

    void setName(String name) {
        this.name = name;
    }
}

class Java extends Programming implements Language, FrameworkLanguage {
    public String getCode() {
        return "Java";
    }
    public void thisframework() {
        System.out.println("JSP ver2.");
    }
}

class Python extends Programming implements Language, FrameworkLanguage {
    public String getCode() {
        return "Python";
    }
    public void thisframework() {
        System.out.println("Django ver2.");
    }
}

class Coder {
    void coding(Language language) {
        System.out.println("coding " + language.getCode());
    }
}

class Framework {
    void thisFramework(FrameworkLanguage programming) {
        programming.thisframework();
    }
}

public class InterfaceCase {
    public static void main(String[] args) {
        Java java = new Java();
        Python python = new Python();

        Framework framework = new Framework();
        framework.thisFramework(java);
        framework.thisFramework(python);
    }
}
