import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class MD5DigestCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("MD5 Message Digest Calculator");
        System.out.print("Enter the text to hash: ");
        String input = scanner.nextLine();
        
        try {
            String md5Hash = calculateMD5(input);
            System.out.println("MD5 Hash: " + md5Hash);
        } catch (NoSuchAlgorithmException e) {
            System.err.println("MD5 algorithm not available");
        }
        
        scanner.close();
    }
    
    public static String calculateMD5(String text) throws NoSuchAlgorithmException {
        // Create MessageDigest instance for MD5
        MessageDigest md = MessageDigest.getInstance("MD5");
        
        // Add text bytes to digest
        md.update(text.getBytes());
        
        // Get the hash's bytes
        byte[] bytes = md.digest();
        
        // Convert bytes to hexadecimal format
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        
        return sb.toString();
    }
}