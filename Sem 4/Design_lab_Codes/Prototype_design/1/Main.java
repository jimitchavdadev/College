import java.util.Scanner;

// Define the Vehicle class
class Vehicle implements Cloneable {
    private String make;
    private String model;
    private int year;

    // Constructor
    public Vehicle(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    // Method to drive the vehicle
    public void drive() {
        System.out.println("Driving the " + year + " " + make + " " + model);
    }

    // Method to clone the vehicle
    @Override
    public Vehicle clone() {
        try {
            return (Vehicle) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new AssertionError(); // Should never happen
        }
    }

    // Method to set the year
    public void setYear(int year) {
        this.year = year;
    }
}

public class Main {
    public static void main(String[] args) {
        // Create a scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt user for vehicle details
        System.out.println("Enter the make of the vehicle:");
        String make = scanner.nextLine();

        System.out.println("Enter the model of the vehicle:");
        String model = scanner.nextLine();

        System.out.println("Enter the year of the vehicle:");
        int year = scanner.nextInt();

        // Create the prototype vehicle
        Vehicle prototypeVehicle = new Vehicle(make, model, year);

        // Clone the prototype vehicle
        Vehicle clonedVehicle = prototypeVehicle.clone();
        // No need to customize the year

        // Drive the cloned vehicle
        clonedVehicle.drive();
    }
}
