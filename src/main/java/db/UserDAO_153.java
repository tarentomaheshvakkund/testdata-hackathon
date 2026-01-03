package db;
import java.sql.*;

public class UserDAO_153 {
    private Connection conn;
    
    public User find(String username) throws SQLException {
        String q = "SELECT * FROM users WHERE username = '" + username + "'";
        return conn.createStatement().executeQuery(q);
    }
}
