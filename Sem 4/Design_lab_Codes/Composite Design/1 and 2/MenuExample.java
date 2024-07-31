import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Component interface
interface MenuComponent {
    void display();
}

// Leaf class representing a single menu item
class MenuItem implements MenuComponent {
    private String name;

    public MenuItem(String name) {
        this.name = name;
    }

    public void display() {
        System.out.println(name);
    }
}

// Composite class representing a menu containing submenus or menu items
class Menu implements MenuComponent {
    private String name;
    private List<MenuComponent> menuComponents = new ArrayList<>();

    public Menu(String name) {
        this.name = name;
    }

    public void add(MenuComponent component) {
        menuComponents.add(component);
    }

    public void remove(MenuComponent component) {
        menuComponents.remove(component);
    }

    public void display() {
        System.out.println("Menu: " + name);
        for (MenuComponent component : menuComponents) {
            component.display();
        }
    }
}

public class MenuExample {
    public static void main(String[] args) {
        // Create main menu
        Menu mainMenu = new Menu("Main Menu");

        // Create submenus
        Menu fileMenu = new Menu("File");
        Menu editMenu = new Menu("Edit");
        Menu viewMenu = new Menu("View");

        // Add submenus to the main menu
        mainMenu.add(fileMenu);
        mainMenu.add(editMenu);
        mainMenu.add(viewMenu);

        // Create menu items for the submenus
        MenuItem newItem = new MenuItem("New");
        MenuItem openItem = new MenuItem("Open");
        MenuItem saveItem = new MenuItem("Save");
        MenuItem exitItem = new MenuItem("Exit");

        MenuItem cutItem = new MenuItem("Cut");
        MenuItem copyItem = new MenuItem("Copy");
        MenuItem pasteItem = new MenuItem("Paste");

        MenuItem zoomInItem = new MenuItem("Zoom In");
        MenuItem zoomOutItem = new MenuItem("Zoom Out");

        // Add menu items to the submenus
        fileMenu.add(newItem);
        fileMenu.add(openItem);
        fileMenu.add(saveItem);
        fileMenu.add(exitItem);

        editMenu.add(cutItem);
        editMenu.add(copyItem);
        editMenu.add(pasteItem);

        viewMenu.add(zoomInItem);
        viewMenu.add(zoomOutItem);

        // Display the main menu
        mainMenu.display();

        // Simulate user interaction by selecting a submenu
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the submenu to display (File/Edit/View): ");
        String selectedMenu = scanner.nextLine().trim().toLowerCase();

        // Display the selected submenu
        switch (selectedMenu) {
            case "file":
                fileMenu.display();
                break;
            case "edit":
                editMenu.display();
                break;
            case "view":
                viewMenu.display();
                break;
            default:
                System.out.println("Invalid submenu selection.");
        }

        scanner.close();
    }
}
