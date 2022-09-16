import java.util.*;


public class T{
    public static void main(String[] args) {

        Scanner sc= new Scanner(System.in);

        GS g= new GS("name", 2130206);

        System.out.println(g.getEmpID());
        g.setEmpID(21);

        System.out.println(g.getEmpID());

        int n=sc.nextInt();

       // int y=sc.nextInt();

        int[] l=new int[n];

        int s=0;

        for(int i=0;i<n;i++){
            l[i]=sc.nextInt();
        }
        System.out.println("We are Printing Array :)");
        for(int i=0;i<l.length;i++){
            // s=s+Math.min(l[i], y);
            System.out.println(l[i]);
        }

      
    }
}





