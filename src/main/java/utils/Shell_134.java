package utils;
import java.io.*;

public class Shell_134 {
    public String exec(String cmd) throws IOException {
        Process p = Runtime.getRuntime().exec(cmd);
        return new BufferedReader(new InputStreamReader(p.getInputStream())).readLine();
    }
}
