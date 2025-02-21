import java.util.Scanner;

public class AccountTest {
    public static void main(String[] args) {
        Account account1 = new Account("Jane Green", 50.00);
        Account account2 = new Account("John Blue", -7.53);

        displayAccount(account1);
        displayAccount(account2);

        Scanner input = new Scanner(System.in);

        System.out.print("enter deposit amount for account1: ");
        double depositAmount = input.nextDouble();
        System.out.printf("%nadding %.2f to account1 balance%n%n",depositAmount);
        account1.deposit(depositAmount);

        displayAccount(account1);
        displayAccount(account2);

        System.out.print("enter deposit amount for account2: ");
        depositAmount = input.nextDouble();
        System.out.printf("%nadding %.2f to account2 balance%n%n",depositAmount);
        account2.deposit(depositAmount);

        displayAccount(account1);
        displayAccount(account2);

    }
    public static void displayAccount(Account accountToDisplay){
        System.out.println("Name: ");
        System.out.println(accountToDisplay.getName());
        System.out.println("balance: ");
        System.out.println(accountToDisplay.getBalance());
    }
}