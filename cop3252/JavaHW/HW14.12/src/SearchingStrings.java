import java.util.Scanner;

public class SearchingStrings {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] letterCount = new int[26];

        System.out.print("Enter a line of text: ");
        String text = scanner.nextLine().toLowerCase();


        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (Character.isLetter(c)) {
                int index = c - 'a';
                letterCount[index]++;
            }
        }


        System.out.println("Letter\tCount");
        for (int i = 0; i < letterCount.length; i++) {
            char letter = (char) ('a' + i);
            System.out.println(letter + "\t\t" + letterCount[i]);
        }
    }
}