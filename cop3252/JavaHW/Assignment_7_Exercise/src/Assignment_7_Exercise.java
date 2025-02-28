import java.util.InputMismatchException;
import java.util.Scanner;
public class Assignment_7_Exercise {
        static class DivideByZeroWithExceptionHandling {
            private static int numerator;
            private static int denominator;

            public static int quotient(int numerator, int denominator) throws ArithmeticException {
                return numerator / denominator;
            }

            public static void main(String[] args) {
                Scanner scanner = new Scanner(System.in);
                boolean continueLoop = true;

                do {
                    try {
                        System.out.print("Please enter an integer numerator: ");
                        numerator = scanner.nextInt();
                        System.out.print("Please enter an integer denominator: ");
                        denominator = scanner.nextInt();

                        if (denominator == 0) {
                            throw new ArithmeticException("Oops, can't do that.");
                        }

                        int result = quotient(numerator, denominator);
                        System.out.printf("%nResult: %d / %d = %d%n", numerator, denominator, result);
                        continueLoop = false;
                    } catch (InputMismatchException inputMismatchException) {
                        System.err.printf("%nException: %s%n", inputMismatchException);
                        scanner.nextLine();
                        System.out.printf("You must enter integers. Please try again.%n%n");
                    } catch (ArithmeticException arithmeticException) {
                        System.err.printf("%nException: %s%n", arithmeticException);
                        System.out.printf("Zero is an invalid denominator. Please try again.%n%n");
                    } finally {
                        System.out.println("\nNumerator is " + numerator);
                        System.out.println("Denominator is " + denominator + "\n");
                    }
                } while (continueLoop);
            }
        }

}