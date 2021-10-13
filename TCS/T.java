import java.util.*;

public class T{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int y=sc.nextInt();
        int[] l=new int[n];
        int s=0;
        for(int i=0;i<n;i++){
            l[i]=sc.nextInt();
        }
        for(int i=0;i<l.length;i++){
            s=s+Math.min(l[i], y);
        }

      
    }
}


// 