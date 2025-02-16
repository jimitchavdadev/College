// Currency.java
public interface Currency {
    String getCurrencyCode();
    String getSymbol();
    String format(double amount);
    double convert(double amount, Currency targetCurrency);
}
