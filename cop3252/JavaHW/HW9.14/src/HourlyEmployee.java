public class HourlyEmployee extends EmployeeHierarchy.Employee {
    private double wage;
    private double hours;
    public HourlyEmployee(String firstname, String lastname, String social, double wage, double hours) {
        super(firstname, lastname, social);
        this.hours = hours;
        this.wage = wage;
    }
    public double getWage(){return wage;}
    public double getHours() {return hours;}
    public void setWage(double wage){
        if (wage < 0){
            throw new IllegalArgumentException("wage cannot be negative");
        }
        this.wage = wage;}
    public void setHours(double hours) {
        if (hours < 0 || hours > 168){
            throw new IllegalArgumentException("invalid hours");
        }
        this.hours = hours;}
    public double earnings(){
        return wage * hours;
    }
    public String toString(){
        return String.format("Hourly Employee: " + firstName + " " + lastName + " SSN:" + socialSecurityNumber + "\n" +
                "Hourly wage: " + wage + "\nHours worked: " + hours +
                "\nEarnings: " + earnings());
    }
}
