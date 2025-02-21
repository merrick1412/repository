import java.util.Scanner;

public class InvoiceTest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String num;
        String description;
        int quantity;
        double price;

        System.out.println("Please enter the part number: ");
        num = scanner.nextLine();
        System.out.println("Please enter the part description: ");
        description = scanner.nextLine();
        System.out.println("Please enter the the quantity being ordered: ");
        quantity = scanner.nextInt();
        System.out.println("Please enter the price per part: ");
        price = scanner.nextDouble();
        scanner.nextLine();
        Invoice test = new Invoice(num,description,quantity,price);
        boolean quit = true;
        while (quit) {
            String choice = "";
            System.out.println("Please enter your choice ");
            System.out.println("1: change part number");
            System.out.println("2: view part number");
            System.out.println("3: change description");
            System.out.println("4: view description");
            System.out.println("5: change amount ordered");
            System.out.println("6: view amount ordered");
            System.out.println("7: change price per item");
            System.out.println("8: change price per item");
            System.out.println("9: view invoice total");
            System.out.println("q: quit");

            choice = scanner.nextLine();

            switch (choice){
                case "1": System.out.println("enter new part number: ");
                        test.setPartNum(scanner.next()); break;
                case "2": System.out.println(test.getPartNum());break;

                case "3": System.out.println("enter new description: ");
                        test.setDescription(scanner.next());break;
                case "4": System.out.println(test.getDescription());break;

                case "5": System.out.println("enter new amount: ");
                    test.setQuantity(scanner.nextInt());break;
                case "6": System.out.println(test.getQuantity());break;

                case "7": System.out.println("enter new price: ");
                        test.setPrice(scanner.nextDouble());break;
                case "8": System.out.println(test.getPrice());break;

                case "9": System.out.println("Your total is: ");
                    System.out.println(test.getInvoiceAmount());break;

                case "q": quit = false;break;

            }
        }

    }
}

