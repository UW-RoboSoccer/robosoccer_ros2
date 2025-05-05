make a new branch for each pacakge

# RoboSoccer ROS 2 Workspace

This repository is a full ROS 2 Humble workspace for the RoboCup Humanoid KidSize project, supporting both hardware and MuJoCo-based simulation.

---

## 🏗️ Workspace Structure

```
robosoccer_ros2/
  src/
    robosoccer_behavior/
    robosoccer_bringup/
    robosoccer_control/
    robosoccer_description/
    robosoccer_diagnostics/
    robosoccer_firmware/
    robosoccer_gamecontrol/
    robosoccer_localization/
    robosoccer_motion/
    robosoccer_msgs/
    robosoccer_perception/
    robosoccer_sim/           # MuJoCo simulation package
    robosoccer_world_model/
  .devcontainer/              # VS Code + Docker setup
```

---

## 🚀 Quickstart

### 1. **Native (Ubuntu 22.04 + ROS 2 Humble)**

Install [ROS 2 Humble](https://docs.ros.org/en/humble/Installation.html) and dependencies:

```sh
sudo apt update
sudo apt install python3-colcon-common-extensions python3-vcstool mujoco libmujoco-dev
pip install mujoco
```

Build the workspace:
```sh
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```

### 2. **VS Code Devcontainer (Recommended)**

- Install [Docker](https://docs.docker.com/get-docker/) and [VS Code](https://code.visualstudio.com/)
- Open this repo in VS Code and "Reopen in Container"
- All dependencies are installed automatically

---

## 🕹️ Running Simulation

To launch the MuJoCo simulation node:
```sh
ros2 launch robosoccer_sim sim_mujoco.launch.py
```

To launch the full system (hardware or sim):
```sh
ros2 launch robosoccer_bringup full_system.launch.py
```

---

## 📦 Package Overview

- `robosoccer_sim`: MuJoCo simulation node and model
- `robosoccer_behavior`, `robosoccer_control`, ...: Core robot nodes
- `robosoccer_msgs`: Custom message definitions (extend as needed)
- `robosoccer_bringup`: Launch and config files

---

## 🧑‍💻 Development Tips

- Use the devcontainer for a reproducible environment
- Add your MuJoCo model to `robosoccer_sim/robosoccer_sample.xml`
- Extend nodes with real logic and hardware integration
- For custom messages, see [ROS 2 custom interface tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html)

---

## 🤖 Credits

Built for RoboCup Humanoid League 2024.

---

## 🆘 Troubleshooting

- If you see `ModuleNotFoundError`, check your build and sourcing
- For MuJoCo issues, ensure `mujoco` and `libmujoco-dev` are installed
- For ROS 2 errors, check dependencies in each `package.xml`
