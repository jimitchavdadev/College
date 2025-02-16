// Product
class Phone {
    private String os;
    private int ram;
    private String processor;
    private double screenSize;
    private int battery;

    // Constructor is private to enforce the use of the builder
    private Phone() {}

    // Getters for Phone attributes
    public String getOs() {
        return os;
    }

    public int getRam() {
        return ram;
    }

    public String getProcessor() {
        return processor;
    }

    public double getScreenSize() {
        return screenSize;
    }

    public int getBattery() {
        return battery;
    }

    // Builder
    static class PhoneBuilder {
        private Phone phone = new Phone();

        public PhoneBuilder setOs(String os) {
            phone.os = os;
            return this;
        }

        public PhoneBuilder setRam(int ram) {
            phone.ram = ram;
            return this;
        }

        public PhoneBuilder setProcessor(String processor) {
            phone.processor = processor;
            return this;
        }

        public PhoneBuilder setScreenSize(double screenSize) {
            phone.screenSize = screenSize;
            return this;
        }

        public PhoneBuilder setBattery(int battery) {
            phone.battery = battery;
            return this;
        }

        public Phone build() {
            return phone;
        }
    }
}

