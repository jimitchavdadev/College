import java.util.HashMap;
import java.util.Map;

// Flyweight interface
interface Book {
    void displayInfo();
}

// Concrete Flyweight
class ConcreteBook implements Book {
    private final String title;
    private final String author;
    private final String genre;

    public ConcreteBook(String title, String author, String genre) {
        this.title = title;
        this.author = author;
        this.genre = genre;
    }

    @Override
    public void displayInfo() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Genre: " + genre);
        System.out.println("--------------------------");
    }
}

// Flyweight Factory
class BookFactory {
    private static final Map<String, Book> bookMap = new HashMap<>();

    public static Book getBook(String title, String author, String genre) {
        String key = title + "_" + author + "_" + genre;
        if (!bookMap.containsKey(key)) {
            bookMap.put(key, new ConcreteBook(title, author, genre));
        }
        return bookMap.get(key);
    }
}

// Client code
public class LibraryManagement {
    public static void main(String[] args) {
        // Create and display books
        Book book1 = BookFactory.getBook("Java Programming", "John Doe", "Programming");
        book1.displayInfo();

        Book book2 = BookFactory.getBook("Python Basics", "Jane Smith", "Programming");
        book2.displayInfo();

        Book book3 = BookFactory.getBook("Harry Potter", "J.K. Rowling", "Fantasy");
        book3.displayInfo();

        // Demonstrate that the same book instance is reused
        Book book4 = BookFactory.getBook("Java Programming", "John Doe", "Programming");
        book4.displayInfo();
    }
}
