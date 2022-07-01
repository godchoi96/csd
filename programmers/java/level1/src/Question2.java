// x만큼 간격이 있는 n개의 숫자
// https://programmers.co.kr/learn/courses/30/lessons/12954?language=java

import java.util.ArrayList;

public class Question2 {
    public long[] solution(int x, int n) {
        long[] answer = {};
        answer = new long[n];

        for (int i = 0; i < n; i++) {
            answer[i] = (long)x * (i + 1);
        }

        return answer;
    }
    public static void main(String[] args) {
        Question2 q2 = new Question2();
        System.out.println(q2.solution(2, 5));
    }
}
