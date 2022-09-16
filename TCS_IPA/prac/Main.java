import java.util.*;
public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int arr[] = new int [n];
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        int counter = 0; 
        Set<Integer> value = new HashSet<Integer>();
        for(int i : arr){
            value.add(i);
        }
        for(int i : value){
            if(value.contains(i + k)){
                ++counter;
            }
        }
        System.out.println(counter);
    }
    }