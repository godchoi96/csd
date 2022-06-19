import java.util.HashMap;
public class MapCase {
    public static void main(String[] args) {
        HashMap<String, String> map_string = new HashMap<>();
        map_string.put("csd", "최승대");
        map_string.put("lde", "이동은");

        MapCase mapcase = new MapCase();
        mapcase.print_map(map_string);

    }
    public void print_map(HashMap<String, String> a) {
        System.out.println(a);
    }
}
