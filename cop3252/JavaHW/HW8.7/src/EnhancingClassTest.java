public class EnhancingClassTest {
    private static void displayTime(String header, EnhancingClass.Time2 t) {
        System.out.printf("%s%n %s%n %s%n", header, t.toUniversalString(), t.toString());
    }

    public static void main(String[] args) {
        EnhancingClass.Time2 t1 = new EnhancingClass.Time2();
        displayTime("before Incrementing Minute",t1);
        t1.incrementMinute();
        displayTime("Incrementing Minute",t1);
        t1.incrementHour();
        displayTime("Incremented hour",t1);
        EnhancingClass.Time2 t2 = new EnhancingClass.Time2(86399);
        displayTime("before next day",t2);
        t2.tick();
        displayTime("after tick",t2);
    }
}
