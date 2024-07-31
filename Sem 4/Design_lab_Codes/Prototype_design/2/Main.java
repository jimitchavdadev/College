import java.util.Scanner;

// Abstract base class for electronics
abstract class Electronics implements Cloneable {
    private String brand;
    private String model;
    private int year;

    // Constructor
    public Electronics(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    // Getter method for brand
    public String getBrand() {
        return brand;
    }

    // Getter method for model
    public String getModel() {
        return model;
    }

    // Getter method for year
    public int getYear() {
        return year;
    }

    // Method to get description of the electronics
    public abstract String getDescription();

    // Clone method
    @Override
    public Electronics clone() {
        try {
            return (Electronics) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new AssertionError(); // Should never happen
        }
    }

    // Method to set the year
    public void setYear(int year) {
        this.year = year;
    }
}

// Concrete subclass for television
class Television extends Electronics {
    private int screenSize;

    // Constructor
    public Television(String brand, String model, int year, int screenSize) {
        super(brand, model, year);
        this.screenSize = screenSize;
    }

    // Override method to get description
    @Override
    public String getDescription() {
        return "Television - " + getBrand() + " " + getModel() + ", Year: " + getYear() + ", Screen Size: " + screenSize
                + " inches";
    }
}

// Concrete subclass for smartphone
class Smartphone extends Electronics {
    private String processor;

    // Constructor
    public Smartphone(String brand, String model, int year, String processor) {
        super(brand, model, year);
        this.processor = processor;
    }

    // Override method to get description
    @Override
    public String getDescription() {
        return "Smartphone - " + getBrand() + " " + getModel() + ", Year: " + getYear() + ", Processor: " + processor;
    }
}

public class Main {
    public static void main(String[] args) {
        // Create a scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt user for electronics details
        System.out.println("Enter the type of electronics (television/smartphone):");
        String type = scanner.nextLine();

        System.out.println("Enter the brand of the electronics:");
        String brand = scanner.nextLine();

        System.out.println("Enter the model of the electronics:");
        String model = scanner.nextLine();

        System.out.println("Enter the year of the electronics:");
        int year = scanner.nextInt();
        scanner.nextLine(); // Consume newline character

        // Create the prototype electronics object based on user input
        Electronics prototypeElectronics;
        if (type.equalsIgnoreCase("television")) {
            System.out.println("Enter the screen size of the television (in inches):");
            int screenSize = scanner.nextInt();
            prototypeElectronics = new Television(brand, model, year, screenSize);
        } else if (type.equalsIgnoreCase("smartphone")) {
            System.out.println("Enter the processor of the smartphone:");
            String processor = scanner.nextLine();
            prototypeElectronics = new Smartphone(brand, model, year, processor);
        } else {
            System.out.println("Invalid electronics type.");
            return;
        }

        // Clone the prototype electronics
        Electronics clonedElectronics = prototypeElectronics.clone();
        // Customize if necessary
        System.out.println("Enter the year of the cloned electronics:");
        int clonedYear = scanner.nextInt();
        clonedElectronics.setYear(clonedYear);

        // Display the cloned electronics
        System.out.println("Cloned electronics:");
        System.out.println(clonedElectronics.getDescription());
    }
}
