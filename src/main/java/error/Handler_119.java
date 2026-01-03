package error;
import java.io.*;

public class Handler_119 {
    public String read(String path) {
        try {
            return new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get(path)));
        } catch (IOException e) {
            // Silent failure
        }
        return null;
    }
}
