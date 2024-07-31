import java.util.Scanner;

public class Property {
    private String type;
    private double price;
    private double area;
    private int bedrooms;
    private int bathrooms;
    
    private Property(PropertyBuilder builder) {
        this.type = builder.type;
        this.price = builder.price;
        this.area = builder.area;
        this.bedrooms = builder.bedrooms;
        this.bathrooms = builder.bathrooms;
    }
     
    public String getType() {
        return type;
    }
    
    public double getPrice() {
        return price;
    }
    
    public double getArea() {
        return area;
    }
    
    public int getBedrooms() {
        return bedrooms;
    }
    
    public int getBathrooms() {
        return bathrooms;
    }
    
    public static class PropertyBuilder {
        private String type;
        private double price;
        private double area;
        private int bedrooms;
        private int bathrooms;
        
        public PropertyBuilder(String type, double price, double area) {
            this.type = type;
            this.price = price;
            this.area = area;
        }
        
        public PropertyBuilder bedrooms(int bedrooms) {
            this.bedrooms = bedrooms;
            return this;
        }
        
        public PropertyBuilder bathrooms(int bathrooms) {
            this.bathrooms = bathrooms;
            return this;
        }
        
        public Property build() {
            return new Property(this);
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter property type:");
        String type = scanner.nextLine();
        
        System.out.println("Enter property price:");
        double price = scanner.nextDouble();
        
        System.out.println("Enter property area:");
        double area = scanner.nextDouble();
        
        System.out.println("Enter number of bedrooms:");
        int bedrooms = scanner.nextInt();
        
        System.out.println("Enter number of bathrooms:");
        int bathrooms = scanner.nextInt();
        
        Property property = new Property.PropertyBuilder(type, price, area)
                                .bedrooms(bedrooms)
                                .bathrooms(bathrooms)
                                .build();
        
        System.out.println("\nProperty details:");
        System.out.println("Type: " + property.getType());
        System.out.println("Price: $" + property.getPrice());
        System.out.println("Area: " + property.getArea() + " sq. ft.");
        System.out.println("Bedrooms: " + property.getBedrooms());
        System.out.println("Bathrooms: " + property.getBathrooms());
        
        scanner.close();
    }
}