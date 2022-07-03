// 핸드폰 번호 가리기
// https://programmers.co.kr/learn/courses/30/lessons/12948?language=java

public class Question4 {
    public String solution(String phone_number) {
        String answer = "";
        String temp = phone_number.substring(phone_number.length() - 4, phone_number.length());

        for (int i = 0; i < phone_number.length() - 4; i++) {
            answer += '*';
        }
        answer += temp;
        return answer;
    }
    public static void main(String[] args) {
        Question4 q4 = new Question4();
        System.out.println(q4.solution("01033334444"));
        System.out.println(q4.solution("027778888"));
    }
}
