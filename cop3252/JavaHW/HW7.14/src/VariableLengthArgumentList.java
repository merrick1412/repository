public class VariableLengthArgumentList {
    public static void main(String[] args) {
        product(1,2,3,4);
        product(1,2,3,4,5,6,7);
        product(1,1,1,1);
        product(2,37);
    }

    static void product(int... nums){
        System.out.println("product: ");
        int product = 0;

        for (int i = 0; i < nums.length; i++){
            if (product == 0){
                product = 1;
            }
            product = product * nums[i];
        }
        System.out.println(product);
    }
}