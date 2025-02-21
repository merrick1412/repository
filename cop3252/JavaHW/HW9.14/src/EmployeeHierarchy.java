public class EmployeeHierarchy {
    public static class Employee{
         final String firstName;
         final String lastName;
         final String socialSecurityNumber;

        String getFirstName(){
            return firstName;
        }
        String getLastName(){
            return lastName;
        }
        String getSocialSecurityNumber(){
            return socialSecurityNumber;
        }
        public Employee(String firstname, String lastname, String social){
            firstName = firstname;
            lastName = lastname;
            socialSecurityNumber = social;
        }

    }
    public static class BasePlusComissionEmployee extends Employee {
            public BasePlusComissionEmployee(String firstname, String lastname, String social,
                                             double grossSales, double commissionRate, double baseSalary){
                super(firstname,lastname,social);
                this.commissionRate = commissionRate;
                this.baseSalary = baseSalary;
                this.grossSales = grossSales;
            }
        private double commissionRate;
        private double grossSales;
        private double baseSalary;
        public void setGrossSales(double grossSales){
            if (grossSales < 0.0){
                throw new IllegalArgumentException("gross sales cannot be below 0");
            }
            this.grossSales = grossSales;
        }
        public void setCommissionRate(double commissionRate){
            if (commissionRate <= 0.0){
                throw new IllegalArgumentException("commission rate cannot be below 0");
            }
            this.commissionRate = commissionRate;
        }
        public void setBaseSalary(double baseSalary){
            if (baseSalary <= 0){
                throw new IllegalArgumentException("base salary cannot be at/below 0");
            }
            this.baseSalary = baseSalary;
        }
        public double getGrossSales() {return grossSales;}
        public double getCommissionRate() {return commissionRate;}
        public double getBaseSalary() {return baseSalary;}
        public double earnings() {return commissionRate * grossSales + baseSalary;}
        public String toString(){
            return String.format("Base Salaried Employee: " + firstName + " " + lastName + " SSN:" + socialSecurityNumber + "\n" +
                    "Sales and commission rate: " + grossSales + " " + commissionRate
                    + "\n" + "Base salary: " + baseSalary + "\nEarnings: " + earnings());
        }
    }
    public static class ComissionEmployee extends Employee{

        public ComissionEmployee(String firstname, String lastname, String social,
                                 double grossSales, double commissionRate) {
            super(firstname, lastname, social);
            this.grossSales = grossSales;
            this.commissionRate = commissionRate;
        }
        private double commissionRate;
        private double grossSales;
        public void setGrossSales(double grossSales){
            if (grossSales < 0.0){
                throw new IllegalArgumentException("gross sales cannot be below 0");
            }
            this.grossSales = grossSales;
        }
        public void setCommissionRate(double commissionRate){
            if (commissionRate <= 0.0){
                throw new IllegalArgumentException("commission rate cannot be below 0");
            }
            this.commissionRate = commissionRate;
        }
        public double getGrossSales() {return grossSales;}
        public double getCommissionRate() {return commissionRate;}
        public double earnings() {return commissionRate * grossSales;}
        public String toString(){
            return String.format("Commission Employee: " + firstName + " " + lastName + " SSN:" + socialSecurityNumber + "\n" +
                    "Sales and commission rate: " + grossSales + " " + commissionRate
                    + "\n" + "Earnings: " + earnings());
        }
    }

}