import java.math.BigInteger;
import java.util.Random;

public class ElGamalEncryption {

    static BigInteger gcd(BigInteger a, BigInteger b) {
        if (b.equals(BigInteger.ZERO)) {
            return a;
        } else {
            return gcd(b, a.mod(b));
        }
    }

    static BigInteger genKey(BigInteger q) {
        Random rand = new Random();
        BigInteger key;
        do {
            key = new BigInteger(q.bitLength(), rand);
        } while (key.compareTo(q) >= 0 || !gcd(q, key).equals(BigInteger.ONE));

        return key;
    }

    static BigInteger power(BigInteger a, BigInteger b, BigInteger c) {
        return a.modPow(b, c);
    }

    static Object[] encrypt(String msg, BigInteger q, BigInteger h, BigInteger g) {
        Random rand = new Random();
        BigInteger k = genKey(q);
        BigInteger s = power(h, k, q);
        BigInteger p = power(g, k, q);

        BigInteger[] enMsg = new BigInteger[msg.length()];
        for (int i = 0; i < msg.length(); i++) {
            enMsg[i] = BigInteger.valueOf((int) msg.charAt(i)).multiply(s);
        }

        System.out.println("g^k used : " + p);
        System.out.println("g^ak used : " + s);
        return new Object[] { enMsg, p };
    }

    static String decrypt(BigInteger[] enMsg, BigInteger p, BigInteger key, BigInteger q) {
        StringBuilder drMsg = new StringBuilder();
        BigInteger h = power(p, key, q);

        for (BigInteger value : enMsg) {
            drMsg.append((char) value.divide(h).intValue());
        }

        return drMsg.toString();
    }

    public static void main(String[] args) {
        Random rand = new Random();
        String msg = "encryption";
        System.out.println("Original Message : " + msg);

        BigInteger q = new BigInteger(100, rand);
        BigInteger g = new BigInteger(q.bitLength(), rand).mod(q);

        BigInteger key = genKey(q);
        BigInteger h = power(g, key, q);

        System.out.println("g used : " + g);
        System.out.println("g^a used : " + h);

        Object[] encryptedData = encrypt(msg, q, h, g);
        BigInteger[] enMsg = (BigInteger[]) encryptedData[0];
        BigInteger p = (BigInteger) encryptedData[1];

        String decryptedMsg = decrypt(enMsg, p, key, q);
        System.out.println("Decrypted Message : " + decryptedMsg);
    }
}