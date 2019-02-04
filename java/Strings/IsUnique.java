public class IsUnique {
    
    public static void main(String []args)
    {
        System.out.println(isUnique("helo"));
    }
    
    //O(n)
    public static boolean isUnique(String str)
    {
        int[] count = new int[128];
        for(int i = 0; i < str.length(); i++)
        {
            char c = str.charAt(i);
            if(count[c] == 1)
                return false;
            else
                count[c] = 1;
        }
        return true;
    }
}