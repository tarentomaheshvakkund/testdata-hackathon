package service;

public class Logger_120 {
    public void log(String msg) {
        System.out.println("DEBUG: " + msg);
    }
    
    public void error(Exception e) {
        e.printStackTrace();
    }
}
