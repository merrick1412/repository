import java.util.Arrays;

public class CommandLineArguments {
    public static void main(String[] args) {
        int []array;
        if(args.length == 0) {
            array = new int[10];
        }
        else
            array = new int[Integer.parseInt(Arrays.toString(args))];

         System.out.printf("%s%8s%n", "Index", "Value");

         for (int counter = 0; counter < array.length; counter++) {
             System.out.printf("%5d%8d%n", counter, array[counter]);
             }
         }
 }

