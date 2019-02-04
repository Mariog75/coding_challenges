import java.util.Arrays;
public class CheckPermutation {

    public static void main(String []args)
    {
        System.out.println(checkPermutation("hello", "leohe"));
    }

    public static boolean checkPermutation(String s1, String s2)
    {
        if(s1.length() != s2.length())
            return false;
        char[] char1 = s1.toCharArray();
        char[] char2 = s2.toCharArray();

        Arrays.sort(char1);
        Arrays.sort(char2);

        for(int i = 0; i < char1.length; i++)
        {
            if(char1[i] != char2[i])
                return false;
        }

        return true;
    }
}