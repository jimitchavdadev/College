import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Choose an operating system (Windows, Linux, MacOS): ");
        String osChoice = scanner.next().toLowerCase();

        OperatingSystem operatingSystem;

        switch (osChoice) {
            case "windows":
                operatingSystem = new WindowsOperatingSystem();
                break;
            case "linux":
                operatingSystem = new LinuxOperatingSystem();
                break;
            case "macos":
                operatingSystem = new MacOSOperatingSystem();
                break;
            default:
                System.out.println("Invalid operating system choice. Exiting.");
                return;
        }

        operatingSystem.printChosenOperatingSystem();
    }
}
