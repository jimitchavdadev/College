import java.util.BitSet;

public class BruteForceSDES {

    // Function to brute force the key
    public static void bruteForce(BitSet ciphertext, BitSet knownPlaintext) {
        System.out.println("Starting brute force attack...");

        for (int i = 0; i < 1024; i++) {
            // Generate a 10-bit key from the loop index
            String binaryKey = String.format("%10s", Integer.toBinaryString(i)).replace(' ', '0');
            BitSet key = SDESEncryption.bitSetFromString(binaryKey, 10); // Use SDESEncryption

            // Decrypt the ciphertext using the current key
            BitSet decryptedText = SDESEncryption.decrypt(ciphertext, key); // Use SDESEncryption

            // Print each key
            System.out.print("Trying key: ");
            SDESEncryption.printBinary(key, 10); // Use SDESEncryption

            // Compare with the known plaintext
            if (decryptedText.equals(knownPlaintext)) {
                System.out.println("Key found!");
                System.out.print("Key: ");
                SDESEncryption.printBinary(key, 10); // Use SDESEncryption
                System.out.print("Decrypted Text: ");
                SDESEncryption.printBinary(decryptedText, 8); // Use SDESEncryption
                return;
            }
        }
        System.out.println("Key not found within 1024 possibilities.");
    }

    public static void main(String[] args) {
        // Known key and plaintext for encryption
        BitSet key = SDESEncryption.bitSetFromString("1010000010", 10); // Use SDESEncryption
        BitSet plaintext = SDESEncryption.bitSetFromString("10111101", 8); // Use SDESEncryption

        System.out.print("Original plaintext: ");
        SDESEncryption.printBinary(plaintext, 8); // Use SDESEncryption

        // Encrypt the plaintext
        BitSet ciphertext = SDESEncryption.encrypt(plaintext, key); // Use SDESEncryption
        System.out.print("Ciphertext: ");
        SDESEncryption.printBinary(ciphertext, 8); // Use SDESEncryption

        // Perform brute force attack
        bruteForce(ciphertext, plaintext);
    }
}
