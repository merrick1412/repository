public class BasePlusComissionEmployeeTest {
    public static void main(String[] args) {
        EmployeeHierarchy.BasePlusComissionEmployee employee = new EmployeeHierarchy.BasePlusComissionEmployee(
                "Bob","Lewis", "333-33-3333", 5000,.04,300);
        System.out.printf("Employee information obtained by get methods:%n");
        System.out.printf("%s %s%n","First Name is",employee.getFirstName());
        System.out.printf("%s %s%n","Last Name is",employee.getLastName());
        System.out.printf("%s %s%n","SSN is",employee.getSocialSecurityNumber());
        System.out.printf("%s %s%n","Gross sales is",employee.getGrossSales());
        System.out.printf("%s %s%n","Commission Rate is",employee.getCommissionRate());
        System.out.printf("%s %s%n","Base Salary is",employee.getBaseSalary());

        employee.setBaseSalary(1000);
        System.out.printf("%s %s%n","Updated info is",employee.toString());
    }
}
