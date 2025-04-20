public class ExtendedEuclidean {
    // Helper class to store results
    static class Result {
        int gcd, x, y;

        Result(int gcd, int x, int y) {
            this.gcd = gcd;
            this.x = x;
            this.y = y;
        }
    }

    // Function implementing the extended Euclidean algorithm
    public static Result extendedEuclid(int a, int b) {
        if (b == 0) {
            return new Result(a, 1, 0); // Base case: gcd(a, 0) = a
        }

        // Recursive call
        Result result = extendedEuclid(b, a % b);

        // Update x and y using the results of the recursion
        int gcd = result.gcd;
        int x1 = result.x;
        int y1 = result.y;

        int x = y1;
        int y = x1 - (a / b) * y1;

        return new Result(gcd, x, y);
    }

    // Function to find the multiplicative inverse of a modulo m
    public static Integer findMultiplicativeInverse(int a, int m) {
        Result result = extendedEuclid(a, m);

        // Check if a and m are coprime
        if (result.gcd != 1) {
            return null; // Inverse does not exist
        }

        // Ensure the result is positive
        int inverse = (result.x % m + m) % m;
        return inverse;
    }

    public static void main(String[] args) {
        // Example 1: Basic GCD calculation
        int a = 56, b = 98;
        Result result = extendedEuclid(a, b);
        System.out.println("GCD: " + result.gcd);
        System.out.println("x: " + result.x);
        System.out.println("y: " + result.y);
        System.out.println("Verification: " + (a * result.x + b * result.y));

        // Example 2: Finding multiplicative inverse
        int num = 11, mod = 26;
        Integer inverse = findMultiplicativeInverse(num, mod);
        if (inverse != null) {
            System.out.println("\nThe multiplicative inverse of " + num + " in Z" + mod + " is: " + inverse);
        } else {
            System.out.println("\nThe multiplicative inverse of " + num + " in Z" + mod + " does not exist.");
        }
    }
}
