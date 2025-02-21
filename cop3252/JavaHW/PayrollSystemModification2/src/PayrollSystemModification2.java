import java.util.Calendar;

public class PayrollSystemModification2 {
    public static void main(String[] args) {
        // Test the classes
        Date date1 = new Date(2, 29, 2000);
        Date date2 = new Date(5, 15, 1985);

        SalariedEmployee salariedEmployee = new SalariedEmployee("John", "Smith", "111-11-1111", date1, 800.00);
        PieceWorker pieceWorker = new PieceWorker("Jane", "Doe", "222-22-2222", date2, 2.50, 200);

        Employee[] employees = {salariedEmployee, pieceWorker};



        for (Employee employee : employees) {
            System.out.println(employee);
            System.out.printf("earned $%,.2f%n%n", employee.earnings());
        }
    }

    static class Date {
        private int month;
        private int day;
        private int year;

        private static final int[] daysPerMonth =
                {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        public Date(int month, int day, int year) {
            if (month <= 0 || month > 12) {
                throw new IllegalArgumentException("month (" + month + ") must be 1-12");
            }

            if (day <= 0 || (day > daysPerMonth[month] && !(month == 2 && day == 29))) {
                throw new IllegalArgumentException("day (" + day + ") out-of-range for the specified month and year");
            }

            if (month == 2 && day == 29 && !(year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))) {
                throw new IllegalArgumentException("day (" + day + ") out-of-range for the specified month and year");
            }

            this.month = month;
            this.day = day;
            this.year = year;
        }

        public String toString() {
            return String.format("%d/%d/%d", month, day, year);
        }

        public int getMonth() {
            return month;
        }

        public int getDay() {
            return day;
        }

        public int getYear() {
            return year;
        }
    }

    abstract static class Employee {
        private String firstName;
        private String lastName;
        private String socialSecurityNumber;
        private Date birthDate;

        public Employee(String firstName, String lastName, String socialSecurityNumber, Date birthDate) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.socialSecurityNumber = socialSecurityNumber;
            this.birthDate = birthDate;
        }

        public void setBirthDate(Date birthDate) {
            this.birthDate = birthDate;
        }

        public Date getBirthDate() {
            return birthDate;
        }

        public String getFirstName() {
            return firstName;
        }

        public String getLastName() {
            return lastName;
        }

        public String getSocialSecurityNumber() {
            return socialSecurityNumber;
        }

        @Override
        public String toString() {
            return String.format("%s %s%nsocial security number: %s", getFirstName(), getLastName(), getSocialSecurityNumber());
        }

        public abstract double earnings();
    }

    static class SalariedEmployee extends Employee {
        private double weeklySalary;

        public SalariedEmployee(String firstName, String lastName, String socialSecurityNumber, Date birthDate, double weeklySalary) {
            super(firstName, lastName, socialSecurityNumber, birthDate);

            if (weeklySalary < 0.0) {
                throw new IllegalArgumentException("Weekly salary must be >= 0.0");
            }

            this.weeklySalary = weeklySalary;
        }

        public double getWeeklySalary() {
            return weeklySalary;
        }

        @Override
        public double earnings() {
            Calendar calendar = Calendar.getInstance();
            int currentMonth = calendar.get(Calendar.MONTH) + 1;

            if (currentMonth == getBirthDate().getMonth()) {
                return getWeeklySalary() + 100.0;
            } else {
                return getWeeklySalary();
            }
        }

        @Override
        public String toString() {
            return String.format("salaried employee: %s%n%s: $%,.2f", super.toString(), "weekly salary", getWeeklySalary());
        }
    }

    static class PieceWorker extends Employee {
        private double wage;
        private int pieces;

        public PieceWorker(String firstName, String lastName, String socialSecurityNumber, Date birthDate, double wage, int pieces) {
            super(firstName, lastName, socialSecurityNumber, birthDate);

            if (wage < 0.0) {
                throw new IllegalArgumentException("Wage per piece must be >= 0.0");
            }
            if (pieces < 0) {
                throw new IllegalArgumentException("Number of pieces must be >= 0");
            }

            this.wage = wage;
            this.pieces = pieces;
        }

        public double getWage() {
            return wage;
        }

        public int getPieces() {
            return pieces;
        }

        @Override
        public double earnings() {
            return getWage() * getPieces();
        }

        @Override
        public String toString() {
            return String.format("Piece worker: %s%n%s: $%,.2f; %s: %d", super.toString(), "wage per piece", getWage(), "pieces produced", getPieces());
        }
    }
}