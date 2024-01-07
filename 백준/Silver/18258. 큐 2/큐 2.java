import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{	   
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st; 
		StringBuilder sb = new StringBuilder(); 
		LinkedList<Integer> q = new LinkedList<Integer>();
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine()," ");
			switch(st.nextToken()) {
				case "push" : 
					q.offer(Integer.parseInt(st.nextToken()));
					break;
				case "pop" :
					try {
						sb.append(q.remove()).append('\n');
					}catch(NoSuchElementException e) {
						sb.append(-1).append('\n');
					}
				break;
				
				case "size" :
					sb.append(q.size()).append('\n');
					break;
					
				case "empty" :
						if(q.isEmpty()) {
							sb.append(1).append('\n');	
						}else {
							sb.append(0).append('\n');	
						}
						break;
						
				case "front" :
					try {
						sb.append(q.getFirst()).append('\n');	
					}catch(NoSuchElementException e) {
						sb.append(-1).append('\n');	
					}
					break;
					
				case "back" :
					try {
						sb.append(q.getLast()).append('\n');	
					}catch(NoSuchElementException e) {
						sb.append(-1).append('\n');	
					}
					break;
			}
		}
		System.out.println(sb.toString());
    }  
}