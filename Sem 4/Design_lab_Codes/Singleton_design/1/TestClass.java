package St;

class Singleton {
    private static Singleton instance;
    private int i;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }

    public int getI() {
        return i;
    }

    public void setI(int i) {
        this.i = i;
    }
}

class TestClass {
    public static void main(String args[]) {
        Singleton s1 = Singleton.getInstance();
        Singleton s2 = Singleton.getInstance();
        s1.setI(5);
        s2.setI(10);
        System.out.println(s1.getI());
        s2.setI(s1.getI() + s2.getI());
        print("s1", s1);
        print("s2", s2);

    }

    static void print(String name, Singleton obj) {
        System.out.println(String.format("Object:%s, Hashcode:%d", name, obj.hashCode()));
    }
}
