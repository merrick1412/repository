import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CoinTossing {
    enum Coin {
        Heads, Tails
    }
    static List<Coin> results = new ArrayList<>();
    public static void main(String[] args) {

        boolean quit = true;
        Scanner input = new Scanner(System.in);
        String choice;


        while(quit){

            System.out.println("Press 1 to toss a coin, and 2 to see results");
            choice = input.next();
            switch (choice){
                case "1": results.add(Flip()); break;

                case "2": PrintResults(); quit = false; break;
            }
        }
    }

    static Coin Flip(){
        double rand = Math.random();
        if (rand < 0.5){
            return Coin.Heads;
        }
        else
            return Coin.Tails;
    }
    static void PrintResults(){
        for (Coin t : results){
            System.out.println(t);
        }
        int heads = 0;
        int tails = 0;
        for (Coin t : results){
            if (t == Coin.Heads){
                heads++;
            }
            else
                tails++;
        }
        System.out.println("Heads: ");
        System.out.println(heads);
        System.out.println("Tails: ");
        System.out.println(tails);
    }
}