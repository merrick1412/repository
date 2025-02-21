public class HourlyEmployeeTest {
    public static void main(String[] args) {
        HourlyEmployee employee = new HourlyEmployee(
                "Bob","Lewis", "333-33-3333", 20.00, 70);
        System.out.printf("Employee information obtained by get methods:%n");
        System.out.printf("%s %s%n","First Name is",employee.getFirstName());
        System.out.printf("%s %s%n","Last Name is",employee.getLastName());
        System.out.printf("%s %s%n","SSN is",employee.getSocialSecurityNumber());
        System.out.printf("%s %s%n","Hours worked is",employee.getHours());
        System.out.printf("%s %s%n","Hourly Rate is",employee.getWage());


        employee.setHours(165);
        System.out.printf("%s %s%n","Updated info is",employee.toString());
    }
}
