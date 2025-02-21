import java.util.Scanner;

public class SalesCommissions {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double[] salesArray = {5000, 7000, 5500, 10500, 2000, 4000,
                            4500,8000,11000,6000};
        int[] counter = {0,0,0,0,0,0,0,0,0};
        for (int i = 0; i < 10; i++){
            double current = totalSalary(salesArray[i]);
            counter[returnBracket(current)]++;
        }
        System.out.print("200-299: ");
        System.out.println(counter[0]);
        System.out.print("300-399: ");
        System.out.println(counter[1]);
        System.out.print("400-499: ");
        System.out.println(counter[2]);
        System.out.print("500-599: ");
        System.out.println(counter[3]);
        System.out.print("600-699: ");
        System.out.println(counter[4]);
        System.out.print("700-799: ");
        System.out.println(counter[5]);
        System.out.print("800-899: ");
        System.out.println(counter[6]);
        System.out.print("900-999: ");
        System.out.println(counter[7]);
        System.out.print("1000+: ");
        System.out.println(counter[8]);

    }

    static double totalSalary(double sales){
        System.out.println(0.09 * sales + 200);
                return (0.09 * sales + 200);
    }

    static int returnBracket(double sales){
        if (sales < 300){
            return 0;
        }
        if (sales < 400){
            return 1;
        }
        if (sales < 500){
            return 2;
        }
        if (sales < 600){
            return 3;
        }
        if (sales < 700){
            return 4;
        }
        if (sales < 800){
            return 5;
        }
        if (sales < 900){
            return 6;
        }
        if (sales < 1000){
            return 7;
        }
        else
            return 8;
    }
}