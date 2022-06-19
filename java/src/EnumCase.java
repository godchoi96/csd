public class EnumCase {
    enum FrameWork {
        Django,
        Django_Rest_Framework,
        Spring,
        Spring_Boot
    }
    public static void main(String[] args) {
        System.out.println(FrameWork.Django);
        System.out.println(FrameWork.Django_Rest_Framework);
        System.out.println(FrameWork.Spring);
        System.out.println(FrameWork.Spring_Boot);

        for (FrameWork language: FrameWork.values()) {
            System.out.println(language);
        }
    }
}
