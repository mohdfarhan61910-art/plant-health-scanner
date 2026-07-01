
public class recursion {
    
    public static int findPaths(int n , int m ){
      if( n == m){
        return 1;
      }
      int ways1 = findPaths(n - m, m);
      int ways2 = findPaths(n - 1, m);
      return ways1 + ways2;
    }
    public static void main(String[] args) {
     int n = 4 , m = 2 ;
     System.out.println(findPaths(n, m));
    }
    }

