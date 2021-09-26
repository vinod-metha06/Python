import java.util.*;
public class m {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int l=sc.nextInt();

        int[] a= new int[l];

        for(int i=0;i<l;i++){
            a[i]=sc.nextInt();
        }

        a[0]=sc.nextInt();
        a[l-1]=sc.nextInt();
        System.out.println();
        for(int i=0;i<l;i++){
            System.out.println(a[i]);;
        }

    }
}