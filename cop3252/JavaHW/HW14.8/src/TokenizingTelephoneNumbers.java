import java.util.Scanner;

public class TokenizingTelephoneNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a telephone number in the format (555) 555-5555: ");
        String phoneNumber = scanner.nextLine().trim();

        String digitsOnly = phoneNumber.replaceAll("[^0-9]", "");

        String areaCode = digitsOnly.substring(0, 3);
        String firstThreeDigits = digitsOnly.substring(3, 6);
        String lastFourDigits = digitsOnly.substring(6);

        String concatenatedNumber = areaCode + firstThreeDigits + lastFourDigits;


        System.out.println("Area Code: " + areaCode);
        System.out.println("First Three Digits: " + firstThreeDigits);
        System.out.println("Last Four Digits: " + lastFourDigits);
        System.out.println("Concatenated Phone Number: " + concatenatedNumber);

        scanner.close();
    }
}