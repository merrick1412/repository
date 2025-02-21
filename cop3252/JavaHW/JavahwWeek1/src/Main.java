import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the first integer: ");
        int num1 = scanner.nextInt();

        System.out.println("Enter the second integer: ");
        int num2 = scanner.nextInt();

        System.out.println("Enter the third integer: ");
        int num3 = scanner.nextInt();

        scanner.close();

        int sum = num1 + num2 + num3;
        int average = sum / 3;
        int product = num1 * num2 * num3;

        int smallest = Math.min(Math.min(num1, num2), num3);
        int largest = Math.max(Math.max(num1, num2), num3);

        System.out.println("Sum: " + sum);
        System.out.println("Average: " + average);
        System.out.println("Product: " + product);
        System.out.println("Smallest: " + smallest);
        System.out.println("Largest: " + largest);
    }
}