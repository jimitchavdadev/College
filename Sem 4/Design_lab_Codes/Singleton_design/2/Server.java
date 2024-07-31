public class Server {
    // Private static instance of the Server class
    private static Server instance;

    // Private constructor to prevent instantiation from outside
    private Server() {
        // Initialization code here
    }

    // Static method to get the instance of the Server class
    public static Server getInstance() {
        // Lazy initialization: Create instance if null
        if (instance == null) {
            synchronized (Server.class) {
                if (instance == null) {
                    instance = new Server();
                }
            }
        }
        return instance;
    }

    // Other methods of the Server class can be added here

    public void start() {
        System.out.println("Server started.");
    }

    public void stop() {
        System.out.println("Server stopped.");
    }

    public static void main(String[] args) {
        // Get the instance of the server
        Server server = Server.getInstance();

        // Use the server
        server.start();
        // ... do something with the server

        // Stop the server
        server.stop();
    }
}