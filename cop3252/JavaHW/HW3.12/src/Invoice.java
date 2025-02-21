public class Invoice {

    private String partNum;
    private String description;
    private int quantity;
    private double price;
    public Invoice(String num, String Description, int Quantity, double Price){
        partNum = num;
        description = Description;
        quantity = Quantity;
        price = Price;
    }
    public double getPrice() {
        return price;
    }
    public int getQuantity() {
        return quantity;
    }
    public String getPartNum(){
        return partNum;
    }
    public String getDescription() {
        return description;
    }
    public void setPartNum(String s){
        this.partNum = s;
    }
    public void setDescription(String description) {
        this.description = description;
    }
    public void setPrice(double price) {
        this.price = price;
    }
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public double getInvoiceAmount(){
        if (price < 0){
            price = 0.0;
        }
        if (quantity < 0){
            quantity = 0;
        }
        return quantity*price;
    }
}
