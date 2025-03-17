import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;

public class SecurePRNG {
    private SecureRandom secureRandom;

    public SecurePRNG() {
        try {
            // Use a strong algorithm like SHA1PRNG or NativePRNG
            this.secureRandom = SecureRandom.getInstanceStrong();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("SecureRandom instance could not be created", e);
        }
    }

    // Generate a random integer
    public int getRandomInt() {
        return secureRandom.nextInt();
    }

    // Generate a random integer within a range
    public int getRandomIntInRange(int min, int max) {
        return min + secureRandom.nextInt(max - min + 1);
    }

    // Generate a random byte array
    public byte[] getRandomBytes(int length) {
        byte[] bytes = new byte[length];
        secureRandom.nextBytes(bytes);
        return bytes;
    }

    // Generate a random string (Base64 encoded)
    public String getRandomBase64String(int byteLength) {
        return Base64.getEncoder().encodeToString(getRandomBytes(byteLength));
    }

    public static void main(String[] args) {
        SecurePRNG prng = new SecurePRNG();

        System.out.println("Random Int: " + prng.getRandomInt());
        System.out.println("Random Int (1-100): " + prng.getRandomIntInRange(1, 100));
        System.out.println("Random Bytes (Hex): " + bytesToHex(prng.getRandomBytes(16)));
        System.out.println("Random Base64 String: " + prng.getRandomBase64String(16));
    }

    // Utility function to convert bytes to hex
    private static String bytesToHex(byte[] bytes) {
        StringBuilder hexString = new StringBuilder();
        for (byte b : bytes) {
            hexString.append(String.format("%02x", b));
        }
        return hexString.toString();
    }
}
