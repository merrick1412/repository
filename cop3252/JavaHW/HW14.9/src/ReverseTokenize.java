import java.util.Scanner;

public class ReverseTokenize {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter a line of text:");

        String inputLine = scanner.nextLine();

        scanner.close();

        String[] tokens = inputLine.split("\\s+");

        System.out.println("Tokens in reverse order:");
        for (int i = tokens.length - 1; i >= 0; i--) {
            System.out.println(tokens[i]);
        }
    }
}