import java.util.ArrayList;
import java.util.List;

// Originator class
class SystemState {
    private String version;

    public SystemState(String version) {
        this.version = version;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public Memento saveToMemento() {
        return new Memento(version);
    }

    public void restoreFromMemento(Memento memento) {
        this.version = memento.getVersion();
    }

    // Memento class
    public static class Memento {
        private final String version;

        public Memento(String version) {
            this.version = version;
        }

        public String getVersion() {
            return version;
        }
    }
}

// Caretaker class
class SystemHistory {
    private final List<SystemState.Memento> mementos = new ArrayList<>();

    public void addMemento(SystemState.Memento memento) {
        mementos.add(memento);
    }

    public SystemState.Memento getMemento(int index) {
        return mementos.get(index);
    }
}

public class SystemUpdateExample {
    public static void main(String[] args) {
        // Create originator object
        SystemState system = new SystemState("Version 1.0");

        // Create caretaker object
        SystemHistory history = new SystemHistory();

        // Save initial state
        history.addMemento(system.saveToMemento());

        // Perform system update
        system.setVersion("Version 2.0");

        // Save updated state
        history.addMemento(system.saveToMemento());

        // Perform another system update
        system.setVersion("Version 3.0");

        // Save updated state
        history.addMemento(system.saveToMemento());

        // Restore to previous state
        system.restoreFromMemento(history.getMemento(1));

        // Print current version
        System.out.println("Current version: " + system.getVersion());
    }
}