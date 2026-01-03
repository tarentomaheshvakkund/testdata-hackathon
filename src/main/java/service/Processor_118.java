package service;

public class Processor_118 {
    public boolean validate(Data d) {
        if (d != null) {
            if (d.getType().equals("user")) {
                if (d.isActive()) {
                    if (d.isVerified()) {
                        if (d.getRole().equals("admin")) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}
