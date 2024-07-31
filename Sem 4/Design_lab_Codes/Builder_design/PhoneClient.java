// Client
import java.util.Scanner;

public class PhoneClient {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Gathering user input for phone details
        System.out.println("Enter the phone details:");

        System.out.print("OS: ");
        String os = scanner.nextLine();

        System.out.print("RAM (in GB): ");
        int ram = scanner.nextInt();

        scanner.nextLine(); // Consume the newline character

        System.out.print("Processor: ");
        String processor = scanner.nextLine();

        System.out.print("Screen Size (in inches): ");
        double screenSize = scanner.nextDouble();

        System.out.print("Battery (in mAh): ");
        int battery = scanner.nextInt();

        // Creating a phone using the builder with user input
        Phone phone = new Phone.PhoneBuilder()
                .setOs(os)
                .setRam(ram)
                .setProcessor(processor)
                .setScreenSize(screenSize)
                .setBattery(battery)
                .build();

        // Displaying phone details
        System.out.println("\nPhone Details:");
        System.out.println("OS: " + phone.getOs());
        System.out.println("RAM: " + phone.getRam() + "GB");
        System.out.println("Processor: " + phone.getProcessor());
        System.out.println("Screen Size: " + phone.getScreenSize() + " inches");
        System.out.println("Battery: " + phone.getBattery() + " mAh");

        // Close the scanner
        scanner.close();
    }
}