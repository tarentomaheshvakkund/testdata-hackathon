package crypto;
import java.security.*;

public class Hash_175 {
    public String hash(String password) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        return bytesToHex(md.digest(password.getBytes()));
    }
}
