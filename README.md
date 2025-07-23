# 🛸 Autonomous Drone Navigation in AirSim

This project demonstrates an autonomous drone flying through predefined waypoints and auto-landing using Microsoft's AirSim simulator and Python APIs.

---

## 📽️ Demo Video


---

## 🚀 Project Overview

The drone takes off, navigates between multiple waypoints, and automatically lands at a designated location. The system is designed to be modular and scalable for integration with reinforcement learning or real-world UAV testing.

### ✨ Features

- Multi-waypoint navigation
- Auto take-off and smooth landing
- Configurable waypoint data in JSON format
- AirSim + Unreal Engine simulation
- Extendable for real drone control

---

## 🧠 Tech Stack

- Python 3.10+
- [AirSim](https://github.com/microsoft/AirSim)
- Unreal Engine 4/5 (Blocks/City environment)
- NumPy, JSON
- (Optional) OpenCV for visualization

---

## 📁 Directory Structure

```bash
project-root/
│
├── main.py                  # Main control script
├── config/
│   └── waypoints.json       # JSON file with GPS or local coordinates
├── assets/
│   └── demo_screenshot.png  # Optional image or video preview
└── README.md

```


⚙️ Setup Instructions
1. Clone This Repo
git clone https://github.com/m7hanan/airsim-drone-waypoints.git
cd airsim-drone-waypoints

2. Install Python Dependencies
pip install numpy msgpack-rpc-python

3. Install and Setup AirSim
Download or build AirSim

Open the Blocks or City environment in Unreal Engine

Press Play to start the simulation

Enable Multirotor mode

Run the Simulation
python main.py

Output:
Drone will auto-takeoff

Navigate 3 waypoints

Hover and land at final point

(Optional) Save flight path or images

📌 Waypoint Configuration
Waypoints are defined in config/waypoints.json:

{
  "waypoints": [
    { "x": 0, "y": 0, "z": -10 },
    { "x": 10, "y": 5, "z": -10 },
    { "x": 20, "y": 0, "z": -10 }
  ]
}


🛠️ Future Improvements
Obstacle avoidance using depth camera

Live camera stream with YOLO object detection

Real drone integration with PX4


📜 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Hanan
University of Colombo | AI + Drone Enthusiast
📧 m7hanan@gmail.com

