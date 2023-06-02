import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException{	  
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		Queue<Integer> q = new PriorityQueue<>(new Comparator<Integer>() {
			@Override
			// o1 < o2 == -1 : 음수 
			// o1 = o2 == 0 : 0 
			// o1 > o2 == 1 : 양수
			//return값이 -1이면 우선순위를 높이고 1이면 우선순위를 낮춘다는 뜻.
			public int compare(Integer o1, Integer o2) {
				if(Math.abs(o1) == Math.abs(o2)) {
					return (o1 < o2) ? -1 : 1; 
				}else {
					return (Math.abs(o1) < Math.abs(o2)) ? -1 : 1;   
				}
			}
		});
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			
			if(x != 0) {
				q.add(x);
			}else if(x == 0){
				
				if(q.size() != 0) {
					sb.append(q.poll()).append('\n');
				}else if(q.size() == 0) {
					sb.append(0).append('\n');
				}
			}
		}
		System.out.println(sb);
	}
}