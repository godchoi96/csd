// 행렬의 덧셈
// https://programmers.co.kr/learn/courses/30/lessons/12950?language=java

import java.util.Arrays;

public class Question3 {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = {};
        answer = new int[arr1.length][arr1[0].length];

        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr1[i].length; j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        return answer;

    }
    public static void main(String[] args) {
        Question3 q3 = new Question3();
        int[][] arr1 = new int[][] {{1, 2}, {2, 3}};
        int[][] arr2 = new int[][] {{3, 4}, {5, 6}};
        int[][] answer = q3.solution(arr1, arr2);

        System.out.println(Arrays.deepToString(answer));
    }
}
