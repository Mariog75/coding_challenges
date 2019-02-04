import com.sun.jdi.connect.IllegalConnectorArgumentsException;

public class IsPalindrome {

    public static void main(String []args)
    {
        System.out.println(isPalindrome("racecar"));
    }

    public static boolean isPalindrome(String str)
    {
        int s = 0;
        int f = str.length()-1;

        return isPalindrome(str, s, f);
    }

    private static boolean isPalindrome(String str, int s, int f)
    {
        if(str.charAt(s) != str.charAt(f))
            return false;

        if(f-s-1 == 1)
            return true;
        
        return isPalindrome(str, s+1, f-1);
    }
}