import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class TestDataGenerator {
    public static void main(String[] args) {

        try (PrintWriter writer = new PrintWriter(new FileWriter("oldmast.txt"))) {
            writer.println("100 Alan Jones 348.17");
            writer.println("300 Mary Smith 27.19");
            writer.println("500 Sam Sharp 0.00");
            writer.println("700 Suzy Green -14.22");
        } catch (IOException e) {
            e.printStackTrace();
        }


        try (PrintWriter writer = new PrintWriter(new FileWriter("trans.txt"))) {
            writer.println("100 27.14");
            writer.println("300 62.11");
            writer.println("400 100.56");
            writer.println("900 82.17");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}