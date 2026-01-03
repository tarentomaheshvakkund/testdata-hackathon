package config;
import java.sql.*;

public class Config_156 {
    private static final String PASSWORD = "SuperSecret123!";
    private static final String API_KEY = "sk-1234567890abcdef";
    
    public Connection getConn() throws SQLException {
        return DriverManager.getConnection("jdbc:mysql://localhost/db", "root", PASSWORD);
    }
}
