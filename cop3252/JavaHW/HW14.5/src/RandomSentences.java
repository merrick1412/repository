import java.util.Random;

public class RandomSentences {
    public static void main(String[] args) {
        String[] articles = {"the", "a", "an"};
        String[] nouns = {"cat", "dog", "man", "woman", "house", "car"};
        String[] verbs = {"runs", "jumps", "sleeps", "eats", "drives"};
        String[] prepositions = {"on", "over", "under", "behind", "in"};

        Random random = new Random();

        for (int i = 0; i < 20; i++) {
            String sentence = generateSentence(articles, nouns, verbs, prepositions, random);
            System.out.println(sentence);
        }
    }
    public static String generateSentence(String[] articles, String[] nouns, String[] verbs, String[] prepositions, Random random) {
        StringBuilder sb = new StringBuilder();

        String article = articles[random.nextInt(articles.length)];
        String noun1 = nouns[random.nextInt(nouns.length)];
        String verb = verbs[random.nextInt(verbs.length)];
        String preposition = prepositions[random.nextInt(prepositions.length)];
        String article2 = articles[random.nextInt(articles.length)];
        String noun2 = nouns[random.nextInt(nouns.length)];

        sb.append(capitalize(article)).append(" ")
                .append(noun1).append(" ")
                .append(verb).append(" ")
                .append(preposition).append(" ")
                .append(article2).append(" ")
                .append(noun2).append(".");
        return sb.toString();
    }

    public static String capitalize(String line) {
        return Character.toUpperCase(line.charAt(0)) + line.substring(1);
    }
}