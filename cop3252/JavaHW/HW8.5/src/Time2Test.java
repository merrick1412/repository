public class Time2Test {
    public static void main(String[] args) {
        ModifyingInternalDataRepresentation.Time2 t1 = new ModifyingInternalDataRepresentation.Time2(); // 00:00:00
        ModifyingInternalDataRepresentation.Time2 t2 = new ModifyingInternalDataRepresentation.Time2(2); // 02:00:00
        ModifyingInternalDataRepresentation.Time2 t3 = new ModifyingInternalDataRepresentation.Time2(21, 34); // 21:34:00
        ModifyingInternalDataRepresentation.Time2 t4 = new ModifyingInternalDataRepresentation.Time2(12, 25, 42); // 12:25:42
        ModifyingInternalDataRepresentation.Time2 t5 = new ModifyingInternalDataRepresentation.Time2(t4); // 12:25:42

        System.out.println("Constructed with:");
        displayTime("t1: all default arguments", t1);
        displayTime("t2: hour specified; default minute and second", t2);
        displayTime("t3: hour and minute specified; default second", t3);
        displayTime("t4: hour, minute and second specified", t4);
        displayTime("t5: Time2 object t4 specified", t5);

        // attempt to initialize t6 with invalid values
        try {
            ModifyingInternalDataRepresentation.Time2 t6 = new ModifyingInternalDataRepresentation.Time2(27, 74, 99); // invalid values
        } catch (IllegalArgumentException e) {
            System.out.printf("%nException while initializing t6: %s%n", e.getMessage());
        }
    }

    // displays a Time2 object in 24-hour and 12-hour formats
    private static void displayTime(String header, ModifyingInternalDataRepresentation.Time2 t) {
        System.out.printf("%s%n %s%n %s%n", header, t.toUniversalString(), t.toString());
    }
}