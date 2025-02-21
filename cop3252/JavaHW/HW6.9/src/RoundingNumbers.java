import java.util.Scanner;

public class RoundingNumbers {
    public static void main(String[] args) {
        boolean quit = true;
        while (quit){
            System.out.println("press 1 to enter a double, or press q to stop entering numbers");
            String choice = "";
            Scanner input = new Scanner(System.in);
            choice = input.next();
            double num;
            switch (choice){
                case "1":
                    System.out.println("Enter your number: ");
                    num = input.nextDouble();
                    System.out.println("original: ");
                    System.out.println(num);
                    System.out.println("rounded: ");
                    System.out.println(Math.floor(num+0.5));break;

                case "q": quit = false; break;

                default: System.out.println("incorrect input"); break;
            }
        }
    }
}