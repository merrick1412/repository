public class CustomString {
    public static class CustomStringUtils {
        public static int customIndexOf(String str, String target) {
            return customIndexOf(str, target, 0);
        }

        public static int customIndexOf(String str, String target, int fromIndex) {
            int strLength = str.length();
            int targetLength = target.length();

            if (fromIndex >= strLength) {
                return -1;
            }

            for (int i = fromIndex; i <= strLength - targetLength; i++) {
                if (str.substring(i, i + targetLength).equals(target)) {
                    return i;
                }
            }

            return -1;
        }

        public static int customLastIndexOf(String str, String target) {
            return customLastIndexOf(str, target, str.length() - 1);
        }

        public static int customLastIndexOf(String str, String target, int fromIndex) {
            int targetLength = target.length();

            if (fromIndex >= str.length()) {
                fromIndex = str.length() - 1;
            }

            for (int i = fromIndex; i >= 0; i--) {
                if (i + targetLength <= str.length() && str.substring(i, i + targetLength).equals(target)) {
                    return i;
                }
            }
            return -1;
        }

        public static void main(String[] args) {
            String str = "Hello world, hello Java!";
            String target = "hello";


            int index = customIndexOf(str, target);
            System.out.println("Custom indexOf: " + index);


            int lastIndex = customLastIndexOf(str, target);
            System.out.println("Custom lastIndexOf: " + lastIndex);
        }
    }
}