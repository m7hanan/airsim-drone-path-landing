import json
import os
from drone_controller import AirSimDroneController

def load_waypoints():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "../config/waypoints.json")
    
    with open(config_path, "r") as f:
        return json.load(f)

def main():
    drone = AirSimDroneController()

    try:
        drone.takeoff()

        waypoints = load_waypoints()

        for wp in waypoints:
            drone.fly_to_waypoint(*wp, speed=3)

        drone.slow_land()

    except Exception as e:
        print(f" Crash: {e}")
    finally:
        drone.shutdown()

if __name__ == "__main__":
    main()
