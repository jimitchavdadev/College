import java.math.BigInteger;
import java.security.SecureRandom;

public class RSA {

    // Generate a large prime number
    private static BigInteger generatePrime(int bitLength) {
        SecureRandom rand = new SecureRandom();
        return BigInteger.probablePrime(bitLength, rand);
    }

    // Generate RSA keys
    public static BigInteger[] generateKeyPair(int bitLength) {
        BigInteger p = generatePrime(bitLength / 2);
        BigInteger q = generatePrime(bitLength / 2);
        BigInteger n = p.multiply(q);
        BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));

        // Choose public exponent e (commonly 65537)
        BigInteger e = BigInteger.valueOf(65537);

        // Ensure e and phi(n) are coprime (gcd(e, phi(n)) = 1)
        while (e.gcd(phi).compareTo(BigInteger.ONE) != 0) {
            e = e.add(BigInteger.TWO); // Try next odd number
        }

        // Calculate the private exponent d such that e * d ≡ 1 (mod φ(n))
        BigInteger d = e.modInverse(phi);

        // Public key is (e, n), Private key is (d, n)
        return new BigInteger[] { e, n, d };
    }

    // Encrypt a message using the public key (e, n)
    public static BigInteger encrypt(BigInteger message, BigInteger e, BigInteger n) {
        return message.modPow(e, n);
    }

    // Decrypt a message using the private key (d, n)
    public static BigInteger decrypt(BigInteger cipherText, BigInteger d, BigInteger n) {
        return cipherText.modPow(d, n);
    }

    public static void main(String[] args) {
        int bitLength = 512; // Key size in bits

        // Step 1: Generate RSA keys
        BigInteger[] keys = generateKeyPair(bitLength);
        BigInteger e = keys[0]; // Public exponent
        BigInteger n = keys[1]; // Modulus
        BigInteger d = keys[2]; // Private exponent

        System.out.println("Public Key (e, n): (" + e + ", " + n + ")");
        System.out.println("Private Key (d, n): (" + d + ", " + n + ")");

        // Step 2: Encrypt a message (convert string to BigInteger)
        String message = "Hello RSA!";
        BigInteger messageBigInt = new BigInteger(1, message.getBytes()); // Ensuring positive value
        System.out.println("Original Message: " + message);

        BigInteger cipherText = encrypt(messageBigInt, e, n);
        System.out.println("Encrypted Message: " + cipherText);

        // Step 3: Decrypt the message
        BigInteger decryptedMessageBigInt = decrypt(cipherText, d, n);
        String decryptedMessage = new String(decryptedMessageBigInt.toByteArray());
        System.out.println("Decrypted Message: " + decryptedMessage);
    }
}
