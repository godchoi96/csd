class Program {
    String name;

    void setName(String name) {
        this.name = name;
    }
}

class Django extends Program {
    void coding() {
        System.out.println(this.name + " start");
    }
}

class JSP extends Django {
    void coding() {
        System.out.println(this.name + " start in JSP");
    }

    void coding(String code) {
        System.out.println(this.name + " start in JSP by " + code);
    }
}

public class InheritCase {
    public static void main(String[] args) {
        JSP jsp = new JSP();
        jsp.setName("django");
        System.out.println(jsp.name);
        jsp.coding();
        jsp.coding("Java");
    }
}

