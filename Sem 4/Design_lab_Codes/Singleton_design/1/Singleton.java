package St;

public class Singleton{
    private static Singleton soleInst= new Singleton();
    public int i;
    private Singleton(){
        System.out.println("Created");

    }
    public static Singleton getInstance(){
        return soleInst;
    }
    public int getI(){
        return i;
    }
    public static void setSoleInstance(Singleton soleInst){
        Singleton.soleInst=soleInst;
    }
    public void setI(int i){
        this.i=i;
    }
}