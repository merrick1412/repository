public class DateClass {
    public static void main(String[] args) {
        Date date = new Date(1,1,2000);
        date.Print1();
        Date date2 = new Date("June", 30,2002);
        date2.Print2();
        Date date3 = new Date(45,2006);
        date3.Print3();
    }
    public static class Date{
        private int day;
        private int month;
        private int year;
        private String monthString;
        private int totalDays;
        public String[] monthNames = {
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
        };

        public Date(int Day,int Month,int Year){
            day = Day;
            month = Month;
            year = Year;
        }
        public Date(String Month, int Day, int Year){
            monthString = Month;
            day = Day;
            year = Year;
        }

        public Date(int Days, int Year){
            totalDays = Days;
            year = Year;
        }

        public void Print1(){
            System.out.println(month + "/" + day + "/" + year);
        }
        public void Print2(){
            System.out.println(monthString + " " + day + ", "+ year );
        }
        public void Print3(){
            System.out.println(totalDays + " " + year);
        }
    }
}