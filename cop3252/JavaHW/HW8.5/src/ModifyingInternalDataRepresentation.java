public class ModifyingInternalDataRepresentation {
    public static void Main(String[] args) {

    }
    public static class Time2 {

        private int seconds;

        // Time2 no-argument constructor:
        // initializes each instance variable to zero
        public Time2() {
            this(0);    // invoke constructor with three arguments
        }

        // Time2 constructor: hour supplied, minute and second defaulted to 0
        public Time2(int seconds) {
            setSeconds(seconds);    // invoke constructor with three arguments
        }
        public Time2(int hour, int minute, int second){
            setSeconds(hour * 3600 + minute * 60 + second);
        }
        public Time2(int minute, int second){
            this(0, minute, second);
        }
        public void setSeconds(int seconds){
           if (seconds < 0 || seconds >= 24 * 60 * 60){
               throw new IllegalArgumentException("seconds must be between 0 and 86400");
           }
           this.seconds = seconds;
        }

        public int getTotalSeconds(){
            return seconds;
        }

        public String toUniversalString(){
            int hours = seconds / 3600;
            int minutes = (seconds % 3600) / 60;
            int Seconds = seconds % 60;
            return String.format("%02d:%02d:%02d", hours,minutes,seconds);
        }

        public String toString(){
            int hours = seconds / 3600;
            int minutes = (seconds % 3600) / 60;
            int Seconds = seconds % 60;
            return String.format("%02d:%02d:%02d",
                    ((hours == 0 || hours == 12) ? 12 : hours % 12),
                    minutes,seconds, (hours < 12 ? "AM" : "PM"));
        }

        // Time2 constructor: another Time2 object supplied
        public Time2(Time2 time) {
            // invoke constructor with three arguments
            this(time.seconds);
        }

        public int getHour() {
            return seconds / 3600;
        }

        // get minute value
        public int getMinute() {
            return (seconds % 3600) / 60;
        }

        // get second value
        public int getSecond() {
            return seconds % 60;
        }



    }

}