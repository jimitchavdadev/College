// Target interface
interface VirtualMachine {
    void start();
    void stop();
}

// Adaptee 1
class HyperV {
    void powerOn() {
        System.out.println("Hyper-V: Powering on...");
    }
    
    void powerOff() {
        System.out.println("Hyper-V: Powering off...");
    }
}

// Adapter for Hyper-V
class HyperVAdapter implements VirtualMachine {
    private HyperV hyperV;

    public HyperVAdapter(HyperV hyperV) {
        this.hyperV = hyperV;
    }

    @Override
    public void start() {
        hyperV.powerOn();
    }

    @Override
    public void stop() {
        hyperV.powerOff();
    }
}

// Adaptee 2
class VMware {
    void turnOn() {
        System.out.println("VMware: Turning on...");
    }

    void turnOff() {
        System.out.println("VMware: Turning off...");
    }
}

// Adapter for VMware
class VMwareAdapter implements VirtualMachine {
    private VMware vmware;

    public VMwareAdapter(VMware vmware) {
        this.vmware = vmware;
    }

    @Override
    public void start() {
        vmware.turnOn();
    }

    @Override
    public void stop() {
        vmware.turnOff();
    }
}

// Client code
public class Main {
    public static void main(String[] args) {
        // Using the Hyper-V adapter
        HyperV hyperV = new HyperV();
        VirtualMachine hyperVAdapter = new HyperVAdapter(hyperV);
        hyperVAdapter.start();
        hyperVAdapter.stop();

        // Using the VMware adapter
        VMware vmware = new VMware();
        VirtualMachine vmwareAdapter = new VMwareAdapter(vmware);
        vmwareAdapter.start();
        vmwareAdapter.stop();
    }
}
