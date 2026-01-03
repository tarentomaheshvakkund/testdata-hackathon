package xml;
import javax.xml.parsers.*;
import java.io.*;

public class Parser_157 {
    public Document parse(String xml) throws Exception {
        DocumentBuilderFactory f = DocumentBuilderFactory.newInstance();
        return f.newDocumentBuilder().parse(new ByteArrayInputStream(xml.getBytes()));
    }
}
