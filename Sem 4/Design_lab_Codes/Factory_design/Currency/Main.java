import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the amount: ");
        double amount = scanner.nextDouble();

        System.out.print("Choose base currency (USD, EUR, INR): ");
        String baseCurrencyCode = scanner.next().toUpperCase();

        System.out.print("Choose target currency (USD, EUR, INR): ");
        String targetCurrencyCode = scanner.next().toUpperCase();

        Currency baseCurrency;
        Currency targetCurrency;

        switch (baseCurrencyCode) {
            case "USD":
                baseCurrency = new USDCurrency();
                break;
            case "EUR":
                baseCurrency = new EURCurrency();
                break;
            case "INR":
                baseCurrency = new INRCurrency();
                break;
            default:
                System.out.println("Invalid base currency code. Using USD as default.");
                baseCurrency = new USDCurrency();
        }

        switch (targetCurrencyCode) {
            case "USD":
                targetCurrency = new USDCurrency();
                break;
            case "EUR":
                targetCurrency = new EURCurrency();
                break;
            case "INR":
                targetCurrency = new INRCurrency();
                break;
            default:
                System.out.println("Invalid target currency code. Using USD as default.");
                targetCurrency = new USDCurrency();
        }

        System.out.println("Conversion from " + baseCurrencyCode + " to " + targetCurrencyCode + ": "
                + targetCurrency.format(baseCurrency.convert(amount, targetCurrency)));
        scanner.close();
    }
}
