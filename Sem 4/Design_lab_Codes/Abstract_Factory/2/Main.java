import java.util.Scanner;

// Abstract Product: Toy
interface Toy {
    void play();
}

// Concrete Products: Car and Doll
class Car implements Toy {
    @Override
    public void play() {
        System.out.println("Playing with car toy");
    }
}

class Doll implements Toy {
    @Override
    public void play() {
        System.out.println("Playing with doll toy");
    }
}

// Abstract Factory: ToyFactory
interface ToyFactory {
    Toy createToy();
}

// Concrete Factories: CarFactory and DollFactory
class CarFactory implements ToyFactory {
    @Override
    public Toy createToy() {
        return new Car();
    }
}

class DollFactory implements ToyFactory {
    @Override
    public Toy createToy() {
        return new Doll();
    }
}

// Client class to demonstrate usage
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Choose the type of toy to create:");
        System.out.println("1. Car");
        System.out.println("2. Doll");
        int choice = scanner.nextInt();

        ToyFactory toyFactory = null;

        switch (choice) {
            case 1:
                toyFactory = new CarFactory();
                break;
            case 2:
                toyFactory = new DollFactory();
                break;
            default:
                System.out.println("Invalid choice. Exiting...");
                System.exit(1);
        }

        // Create toy using the selected factory
        Toy toy = toyFactory.createToy();
        toy.play();

        scanner.close();
    }
}