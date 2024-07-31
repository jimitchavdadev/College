package FW;

public class Buyer {
	public static void main(String args[])
	{
		Vehicle cycle=VehicleFactory.getVehicle("Cycle");
		cycle.assignColour("Blue");
		cycle.startEngine();
		cycle.assignColour("Black");
		cycle.startEngine();
		
		//Vehicle truck1=VehicleFactory.getVehicle("Car");
		
		Vehicle truck=VehicleFactory.getVehicle("Truck");
		truck.assignColour("Brown");
		truck.startEngine();
		
		Vehicle spaceGrayTruck=VehicleFactory.getVehicle("Truck");
		spaceGrayTruck.assignColour("SpaceGrayTruck");
		spaceGrayTruck.startEngine();
	}
}
