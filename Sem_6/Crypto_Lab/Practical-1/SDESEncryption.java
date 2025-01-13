import java.util.BitSet;

public class SDESEncryption {

    // Helper function to print BitSet as binary string
    public static void printBinary(BitSet bits) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 8; i++) {
            sb.append(bits.get(i) ? "1" : "0");
        }
        System.out.println(sb.toString());
    }

    // 1. P10 Permutation for the 10-bit key
    public static BitSet P10(BitSet key) {
        BitSet permutedKey = new BitSet(10);
        permutedKey.set(0, key.get(2));
        permutedKey.set(1, key.get(4));
        permutedKey.set(2, key.get(1));
        permutedKey.set(3, key.get(6));
        permutedKey.set(4, key.get(3));
        permutedKey.set(5, key.get(9));
        permutedKey.set(6, key.get(0));
        permutedKey.set(7, key.get(8));
        permutedKey.set(8, key.get(7));
        permutedKey.set(9, key.get(5));
        return permutedKey;
    }

    // 2. Circular Left Shift (LS-1) for 5 bits
    public static BitSet leftShift(BitSet halfKey) {
        BitSet shifted = new BitSet(5);
        shifted.set(0, halfKey.get(1));
        shifted.set(1, halfKey.get(2));
        shifted.set(2, halfKey.get(3));
        shifted.set(3, halfKey.get(4));
        shifted.set(4, halfKey.get(0));
        return shifted;
    }

    // 3. P8 Permutation for key subkey generation
    public static BitSet P8(BitSet key) {
        BitSet subKey = new BitSet(8);
        subKey.set(0, key.get(5));
        subKey.set(1, key.get(2));
        subKey.set(2, key.get(6));
        subKey.set(3, key.get(3));
        subKey.set(4, key.get(7));
        subKey.set(5, key.get(4));
        subKey.set(6, key.get(9));
        subKey.set(7, key.get(8));
        return subKey;
    }

    // 4. Key Generation: K1 and K2
    public static BitSet[] generateKeys(BitSet key) {
        BitSet permutedKey = P10(key);
        BitSet left = new BitSet(5);
        BitSet right = new BitSet(5);

        for (int i = 0; i < 5; i++) {
            left.set(i, permutedKey.get(i));
            right.set(i, permutedKey.get(i + 5));
        }

        left = leftShift(left);
        right = leftShift(right);

        BitSet combinedKey1 = new BitSet(10);
        for (int i = 0; i < 5; i++) {
            combinedKey1.set(i, left.get(i));
            combinedKey1.set(i + 5, right.get(i));
        }

        BitSet K1 = P8(combinedKey1);

        left = leftShift(left);
        right = leftShift(right);

        BitSet combinedKey2 = new BitSet(10);
        for (int i = 0; i < 5; i++) {
            combinedKey2.set(i, left.get(i));
            combinedKey2.set(i + 5, right.get(i));
        }

        BitSet K2 = P8(combinedKey2);
        return new BitSet[]{K1, K2};
    }

    // 5. Initial Permutation (IP) of the plaintext
    public static BitSet IP(BitSet data) {
        BitSet permutedData = new BitSet(8);
        permutedData.set(0, data.get(1));
        permutedData.set(1, data.get(5));
        permutedData.set(2, data.get(2));
        permutedData.set(3, data.get(0));
        permutedData.set(4, data.get(3));
        permutedData.set(5, data.get(7));
        permutedData.set(6, data.get(4));
        permutedData.set(7, data.get(6));
        return permutedData;
    }

    // 6. Inverse Initial Permutation (IP-1)
    public static BitSet IP1(BitSet data) {
        BitSet permutedData = new BitSet(8);
        permutedData.set(0, data.get(3));
        permutedData.set(1, data.get(0));
        permutedData.set(2, data.get(2));
        permutedData.set(3, data.get(4));
        permutedData.set(4, data.get(6));
        permutedData.set(5, data.get(1));
        permutedData.set(6, data.get(7));
        permutedData.set(7, data.get(5));
        return permutedData;
    }

    // 7. Expansion and permutation (E/P) for fK function
    public static BitSet EP(BitSet halfBlock) {
        BitSet expanded = new BitSet(8);
        expanded.set(0, halfBlock.get(3));
        expanded.set(1, halfBlock.get(0));
        expanded.set(2, halfBlock.get(1));
        expanded.set(3, halfBlock.get(2));
        expanded.set(4, halfBlock.get(1));
        expanded.set(5, halfBlock.get(2));
        expanded.set(6, halfBlock.get(3));
        expanded.set(7, halfBlock.get(0));
        return expanded;
    }

    // S-Boxes (S0 and S1) for substitution
    public static BitSet S0(BitSet input) {
        int row = (input.get(0) ? 1 : 0) << 1 | (input.get(3) ? 1 : 0);
        int col = (input.get(1) ? 1 : 0) << 1 | (input.get(2) ? 1 : 0);
        int[][] S0 = {
            {1, 0, 3, 2},
            {3, 2, 1, 0},
            {0, 2, 1, 3},
            {3, 1, 3, 2}
        };
        int result = S0[row][col];
        BitSet output = new BitSet(2);
        output.set(0, (result & 0b10) != 0);
        output.set(1, (result & 0b01) != 0);
        return output;
    }

    public static BitSet S1(BitSet input) {
        int row = (input.get(0) ? 1 : 0) << 1 | (input.get(3) ? 1 : 0);
        int col = (input.get(1) ? 1 : 0) << 1 | (input.get(2) ? 1 : 0);
        int[][] S1 = {
            {0, 1, 2, 3},
            {2, 0, 1, 3},
            {3, 0, 1, 0},
            {2, 1, 0, 3}
        };
        int result = S1[row][col];
        BitSet output = new BitSet(2);
        output.set(0, (result & 0b10) != 0);
        output.set(1, (result & 0b01) != 0);
        return output;
    }

    // 8. Function fK
    public static BitSet fK(BitSet data, BitSet subkey) {
        BitSet L = new BitSet(4);
        BitSet R = new BitSet(4);
        for (int i = 0; i < 4; i++) {
            L.set(i, data.get(i));
            R.set(i, data.get(i + 4));
        }

        BitSet expandedR = EP(R);
        expandedR.xor(subkey);

        BitSet left = new BitSet(4);
        BitSet right = new BitSet(4);
        for (int i = 0; i < 4; i++) {
            left.set(i, expandedR.get(i));
            right.set(i, expandedR.get(i + 4));
        }

        BitSet S0Out = S0(left);
        BitSet S1Out = S1(right);

        BitSet combined = new BitSet(4);
        combined.set(0, S0Out.get(0));
        combined.set(1, S1Out.get(0));
        combined.set(2, S0Out.get(1));
        combined.set(3, S1Out.get(1));

        BitSet P4Out = new BitSet(4);
        P4Out.set(0, combined.get(1));
        P4Out.set(1, combined.get(3));
        P4Out.set(2, combined.get(0));
        P4Out.set(3, combined.get(2));

        BitSet newL = (BitSet) L.clone();
        newL.xor(P4Out);

        BitSet result = new BitSet(8);
        for (int i = 0; i < 4; i++) {
            result.set(i, newL.get(i));
            result.set(i + 4, R.get(i));
        }
        return result;
    }

    // 9. Switch function (SW)
    public static BitSet SW(BitSet data) {
        BitSet L = new BitSet(4);
        BitSet R = new BitSet(4);
        for (int i = 0; i < 4; i++) {
            L.set(i, data.get(i));
            R.set(i, data.get(i + 4));
        }

        BitSet result = new BitSet(8);
        for (int i = 0; i < 4; i++) {
            result.set(i, R.get(i));
            result.set(i + 4, L.get(i));
        }
        return result;
    }

    // 10. S-DES Encryption
    public static BitSet encrypt(BitSet plaintext, BitSet key) {
        BitSet[] keys = generateKeys(key);
        BitSet K1 = keys[0];
        BitSet K2 = keys[1];

        BitSet permutedData = IP(plaintext);
        BitSet fK1Result = fK(permutedData, K1);
        BitSet switchedData = SW(fK1Result);
        BitSet fK2Result = fK(switchedData, K2);
        return IP1(fK2Result);
    }

    // 11. S-DES Decryption
    public static BitSet decrypt(BitSet ciphertext, BitSet key) {
        BitSet[] keys = generateKeys(key);
        BitSet K1 = keys[0];
        BitSet K2 = keys[1];

        BitSet permutedData = IP(ciphertext);
        BitSet fK2Result = fK(permutedData, K2);
        BitSet switchedData = SW(fK2Result);
        BitSet fK1Result = fK(switchedData, K1);
        return IP1(fK1Result);
    }

    public static void main(String[] args) {
        BitSet key = new BitSet(10);
        for (int i = 0; i < 10; i++) {
            key.set(i, "1010000010".charAt(i) == '1');
        }

        BitSet plaintext = new BitSet(8);
        for (int i = 0; i < 8; i++) {
            plaintext.set(i, "10111101".charAt(i) == '1');
        }

        System.out.print("Original plaintext: ");
        printBinary(plaintext);

        BitSet ciphertext = encrypt(plaintext, key);
        System.out.print("Ciphertext: ");
        printBinary(ciphertext);

        BitSet decryptedText = decrypt(ciphertext, key);
        System.out.print("Decrypted plaintext: ");
        printBinary(decryptedText);
    }
}

