import java.util.Queue;
import java.util.LinkedList;

class Solution {
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};

    Queue<Integer> queue = new LinkedList<>();

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    public void bfs(){

    }
}
/*
[
    [1, 1, 1, 0],
    [1, 2, 2, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 3],
    [0, 0, 0, 3]
]
*/