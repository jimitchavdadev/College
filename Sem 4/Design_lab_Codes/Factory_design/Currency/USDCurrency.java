// USDCurrency.java

// Concrete implementation of Currency for USD
public class USDCurrency implements Currency {
    @Override
    public String getCurrencyCode() {
        return "USD";
    }

    @Override
    public String getSymbol() {
        return "$";
    }

    @Override
    public String format(double amount) {
        // Implement formatting rules for USD
        // Example: return String.format("$%.2f", amount);
        return "$" + String.format("%.2f", amount);
    }

    @Override
    public double convert(double amount, Currency targetCurrency) {
        // Assume a simple conversion rate for demonstration purposes
        if (targetCurrency.getCurrencyCode().equals("USD")) {
            return amount; // No conversion needed
        } else if (targetCurrency.getCurrencyCode().equals("EUR")) {
            return amount * 0.85; // Conversion rate from USD to EUR
        } else if (targetCurrency.getCurrencyCode().equals("INR")) {
            return amount * 73.50; // Conversion rate from USD to INR
        }
        return amount;
    }
}
