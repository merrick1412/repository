import java.util.Scanner;

public class ComparingStrings {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a line of text: ");
        String line = scanner.nextLine();

        String[] words = line.split("\\s+");

        System.out.println("Words ending with 'ED':");
        for (String word : words) {
            if (word.toLowerCase().endsWith("ed")) {
                System.out.println(word);
            }
        }
    }
}