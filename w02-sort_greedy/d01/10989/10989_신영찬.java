import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //TODO : 배열 만들어서 add
        ArrayList<Integer> arr = new ArrayList<>();
        String nextLine = br.readLine();
        while(nextLine != null) {
            arr.add(Integer.parseInt(nextLine));
            nextLine = br.readLine();
        }

        //TODO : 배열 정렬
        Collections.sort(arr);

        //TODO : 배열 출력
        for(int i = 0; i < arr.size(); i++) {
            bw.write(String.valueOf(arr.get(i)) + '\n');
        }
        bw.flush();
        br.close();
    }
}