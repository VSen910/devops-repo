import java.util.Scanner;

public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) != s.charAt(s.length()-i-1)) {
                System.out.println("Not a palindrome");
                return;
            }
        }
        System.out.println("It is a palindrome");
    }
}
