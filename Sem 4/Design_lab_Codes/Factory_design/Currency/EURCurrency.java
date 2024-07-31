// EURCurrency.java

// Concrete implementation of Currency for EUR
public class EURCurrency implements Currency {
    @Override
    public String getCurrencyCode() {
        return "EUR";
    }

    @Override
    public String getSymbol() {
        return "€";
    }

    @Override
    public String format(double amount) {
        // Implement formatting rules for EUR
        // Example: return String.format("€%.2f", amount);
        return "€" + String.format("%.2f", amount);
    }

    @Override
    public double convert(double amount, Currency targetCurrency) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'convert'");
    }
}
