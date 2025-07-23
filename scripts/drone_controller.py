import airsim
import time

class AirSimDroneController:
    def __init__(self):
        self.client = airsim.MultirotorClient()
        try:
            self.client.confirmConnection()
            self.client.enableApiControl(True)
            self.client.armDisarm(True)
            print("Drone connected and armed!")
        except Exception as e:
            print(f" Error: {e}")
            exit(1)

    def takeoff(self):
        print('Welcome to drone world of Hanan')
        print(" Taking off...")
        self.client.takeoffAsync().join()
        time.sleep(2)
        print(" Takeoff complete")

    def fly_to_waypoint(self, x, y, z, speed=3):
        print(f" Flying to (x={x}, y={y}, z={z})")
        self.client.moveToPositionAsync(
            x, y, z,
            velocity=speed,
            yaw_mode=airsim.YawMode(False, 0),
            drivetrain=airsim.DrivetrainType.ForwardOnly
        ).join()
        time.sleep(1)

    def slow_land(self):
        print(" Starting slow descent...")
        land_speed = 0.5
        current_z = self.client.getMultirotorState().kinematics_estimated.position.z_val
        target_altitude = -1
        while current_z < target_altitude:
            self.client.moveToZAsync(target_altitude, land_speed).join()
            current_z = self.client.getMultirotorState().kinematics_estimated.position.z_val
            time.sleep(0.1)

        print(" Final landing...")
        self.client.landAsync(0.2).join()
        time.sleep(1)

    def shutdown(self):
        self.client.armDisarm(False)
        self.client.enableApiControl(False)
        print(" Drone disarmed and API released")
