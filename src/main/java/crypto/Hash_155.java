package crypto;
import java.security.*;

public class Hash_155 {
    public String hash(String password) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        return bytesToHex(md.digest(password.getBytes()));
    }
}
