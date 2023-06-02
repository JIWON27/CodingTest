import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;

public class Main {
	public static void main(String[] args) throws IOException{	   
		Queue<Integer> pq = new PriorityQueue<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();;
		int N = Integer.parseInt(br.readLine());
		
		for(int i=0; i<N; i++) {
			int x = Integer.parseInt(br.readLine());
			
			if(x != 0) { 
				pq.offer(x);
			}else {
				if(pq.isEmpty()) {
					sb.append(0).append('\n');
				}else {
					int max = pq.poll();
					sb.append(max).append('\n');
				}
			}
		}//end of for
		System.out.println(sb);
    }  
}