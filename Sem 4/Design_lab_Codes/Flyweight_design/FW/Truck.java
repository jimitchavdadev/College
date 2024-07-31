package FW;

public class Truck implements Vehicle{

	private final String MAXSPEED;  //Intrensic property
	private String color;
	
	Truck()
	{
		MAXSPEED="120 km/hr";
	}
	
	@Override
	public void assignColour(String color) {
	this.color=color;	
	}

	@Override
	public void startEngine() {
		System.out.println(color+" colored Truck with Max speed is:"+MAXSPEED);		
	}
	

}
