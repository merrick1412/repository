import java.util.Objects;
import java.util.Scanner;

public class GuessTheNumber {
    public static void main(String[] args) {
        int rand = getRand();
        Scanner input = new Scanner(System.in);

        boolean quit = true;
        while (quit){
            System.out.println("Guess a number between 1 and 1000");
            int choice = input.nextInt();
            if(choice < rand){
                System.out.println("Too low! try again");
            }
            if (choice > rand){
                System.out.println("Too high! try again");
            }
            if (choice == rand){
                String c = "";
                System.out.println("Congratulations. You guessed the number!");
                System.out.println("Would you like to play again? y for yes");

                c = input.next();
                if (c == "y"){
                    rand = getRand();
                }
                else
                    quit = false;

            }
        }
    }

    static int getRand(){
        return (int) (Math.random() * 1000) + 1;
    }
}