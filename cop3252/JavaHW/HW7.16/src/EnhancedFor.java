public class EnhancedFor {
    public static void main(String[] args) {
        double []doubleArray = new double[args.length];
        int count = 0;
        for (String string : args){
            doubleArray[count] = Double.parseDouble(string);
        }
        double sum = 0;
        for (double Double : doubleArray){
            sum += Double;
        }
        System.out.println("the sum is: " + sum);
    }
}