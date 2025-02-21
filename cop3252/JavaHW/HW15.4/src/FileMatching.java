
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
public class FileMatching {
    public static class TransactionRecord {
        private int accountNumber;
        private double amount;

        public TransactionRecord(int accountNumber, double amount) {
            this.accountNumber = accountNumber;
            this.amount = amount;
        }

        public int getAccountNumber() {
            return accountNumber;
        }

        public double getAmount() {
            return amount;
        }
    }
    public static class Account {
        private int accountNumber;
        private String name;
        private double balance;

        public Account(int accountNumber, String name, double balance) {
            this.accountNumber = accountNumber;
            this.name = name;
            this.balance = balance;
        }

        public void combine(TransactionRecord transactionRecord) {
            this.balance += transactionRecord.getAmount();
        }


    }
    public class FileMatch {
        public static void main(String[] args) {
            try (
                    BufferedReader masterReader = new BufferedReader(new FileReader("oldmast.txt"));
                    BufferedReader transactionReader = new BufferedReader(new FileReader("trans.txt"));
                    PrintWriter newMasterWriter = new PrintWriter(new FileWriter("newmast.txt"));
                    PrintWriter logWriter = new PrintWriter(new FileWriter("log.txt"))
            ) {
                String masterLine;
                String transactionLine;

                while ((masterLine = masterReader.readLine()) != null && (transactionLine = transactionReader.readLine()) != null) {
                    String[] masterData = masterLine.split(" ");
                    int masterAccountNumber = Integer.parseInt(masterData[0]);
                    double masterBalance = Double.parseDouble(masterData[2]);

                    String[] transactionData = transactionLine.split(" ");
                    int transactionAccountNumber = Integer.parseInt(transactionData[0]);
                    double transactionAmount = Double.parseDouble(transactionData[1]);

                    if (masterAccountNumber == transactionAccountNumber) {

                        double newBalance = masterBalance + transactionAmount;
                        newMasterWriter.println(masterAccountNumber + " " + masterData[1] + " " + newBalance);
                    } else {

                        logWriter.println("Unmatched transaction record for account number " + transactionAccountNumber);
                    }
                }


                while ((masterLine = masterReader.readLine()) != null) {
                    newMasterWriter.println(masterLine);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

}