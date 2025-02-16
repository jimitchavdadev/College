package FW;
import java.util.HashMap;
public class VehicleFactory {

	private static HashMap<String,Vehicle> hashMap=new HashMap<String,Vehicle>();
	
	public static Vehicle getVehicle(String type)
	{
		Vehicle v=null;
		if(hashMap.containsKey(type))
		{
			v=hashMap.get(type);
		}
		else
		{
		switch(type)
		{
		case "Cycle":
			System.out.println("Cycle is created");
			v=new Cycle();
			break;
		case "Truck":
			System.out.println("Truck is created");
			v=new Truck();
			break;
		default:
			throw new IllegalArgumentException("Vehicle type "+type+" does not exist");
		}
		hashMap.put(type,v);
		}
		return v;
	}
}
