// INRCurrency.java

// Concrete implementation of Currency for INR
public class INRCurrency implements Currency {
    @Override
    public String getCurrencyCode() {
        return "INR";
    }

    @Override
    public String getSymbol() {
        return "₹";
    }

    @Override
    public String format(double amount) {
        // Implement formatting rules for INR
        // Example: return String.format("₹%.2f", amount);
        return "₹" + String.format("%.2f", amount);
    }

    @Override
    public double convert(double amount, Currency targetCurrency) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'convert'");
    }
}
