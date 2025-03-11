import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.SecureRandom;

public class ElGamalDigitalSignature {

    private static final SecureRandom random = new SecureRandom();
    private static final int BIT_LENGTH = 512; // Key size

    public static class KeyPair {
        public BigInteger p, g, y, x; // Public (p, g, y), Private (x)
    }

    public static class Signature {
        public BigInteger r, s; // Signature (r, s)
    }

    // Generate Keys
    public static KeyPair generateKeys() {
        KeyPair keyPair = new KeyPair();

        keyPair.p = BigInteger.probablePrime(BIT_LENGTH, random); // Large prime
        keyPair.g = new BigInteger(BIT_LENGTH - 1, random).mod(keyPair.p); // Generator g
        keyPair.x = new BigInteger(BIT_LENGTH - 2, random).mod(keyPair.p.subtract(BigInteger.ONE)); // Private key x
        keyPair.y = keyPair.g.modPow(keyPair.x, keyPair.p); // Public key y

        return keyPair;
    }

    // Compute hash of message
    private static BigInteger hashMessage(String message, BigInteger p) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] digest = md.digest(message.getBytes());
        return new BigInteger(1, digest).mod(p); // Convert hash to BigInteger
    }

    // Sign a message
    public static Signature sign(String message, KeyPair keyPair) throws Exception {
        BigInteger k, kInv, r, s;
        BigInteger pMinusOne = keyPair.p.subtract(BigInteger.ONE);
        BigInteger h = hashMessage(message, keyPair.p);

        do {
            k = new BigInteger(BIT_LENGTH - 2, random).mod(pMinusOne); // Random k
        } while (!k.gcd(pMinusOne).equals(BigInteger.ONE)); // Ensure k is coprime to (p-1)

        r = keyPair.g.modPow(k, keyPair.p); // r = g^k mod p
        kInv = k.modInverse(pMinusOne); // k^(-1) mod (p-1)
        s = (h.subtract(keyPair.x.multiply(r))).multiply(kInv).mod(pMinusOne); // s = (H(m) - xr) * k^(-1) mod (p-1)

        Signature signature = new Signature();
        signature.r = r;
        signature.s = s;

        return signature;
    }

    // Verify a signature
    public static boolean verify(String message, Signature signature, KeyPair keyPair) throws Exception {
        BigInteger h = hashMessage(message, keyPair.p);
        BigInteger v1 = keyPair.g.modPow(h, keyPair.p); // g^H(m) mod p
        BigInteger v2 = (keyPair.y.modPow(signature.r, keyPair.p).multiply(signature.r.modPow(signature.s, keyPair.p)))
                .mod(keyPair.p); // y^r * r^s mod p

        return v1.equals(v2);
    }

    public static void main(String[] args) throws Exception {
        // Generate keys
        KeyPair keyPair = generateKeys();
        System.out.println("Public Key (p, g, y): (" + keyPair.p + ", " + keyPair.g + ", " + keyPair.y + ")");
        System.out.println("Private Key (x): " + keyPair.x);

        // Message to sign
        String message = "Hello, this is ElGamal digital signature!";
        System.out.println("\nMessage: " + message);

        // Sign the message
        Signature signature = sign(message, keyPair);
        System.out.println("Signature (r, s): (" + signature.r + ", " + signature.s + ")");

        // Verify the signature
        boolean isValid = verify(message, signature, keyPair);
        System.out.println("Signature Valid? " + isValid);
    }
}
