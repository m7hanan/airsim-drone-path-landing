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
