# RoboSoccer Mujoco Simulation

## 1. Install Mujoco and Python Bindings

- **Mujoco Engine:**  
  Download and install Mujoco from [https://mujoco.org/download](https://mujoco.org/download) (requires a free account for a license key).
  - On macOS, you can use Homebrew:
    ```sh
    brew install mujoco
    ```
  - Or download and extract the tarball, then set the `MUJOCO_PY_MUJOCO_PATH` or `MUJOCO_PATH` environment variable if needed.

- **Python Bindings:**  
  Install the Python package (in your ROS2 workspace or virtual environment):
  ```sh
  pip install mujoco numpy
  ```

## 2. Check Meshes

Make sure all `.stl` mesh files referenced in `robosoccer_sample.xml` are present in the `meshes/` directory under `robosoccer_sim`.

## 3. Build Your ROS2 Workspace

From the root of your ROS2 workspace:
```sh
colcon build
source install/setup.bash
```
(Use `setup.zsh` if you use zsh.)

## 4. Run the Mujoco Simulation

From your workspace root:
```sh
ros2 launch robosoccer_sim sim_mujoco.launch.py
```
- This starts the Mujoco simulation node, which loads `robosoccer_sample.xml` and begins publishing `/joint_states` and `/imu/data`.

## 5. Troubleshooting

- If you get errors about missing Mujoco or Python packages, double-check your Python environment and that Mujoco is installed and accessible.
- If you get mesh errors, ensure all referenced `.stl` files are in the correct `meshes/` directory.

## 6. Controlling the Robot

- The simulation node subscribes to `/joint_command` (currently a `std_msgs/String` message).
- You can send joint commands by publishing to this topic, but you may want to update the code to use a more structured message (like `sensor_msgs/JointState` or a custom message).

## 7. Customizing

- To use a different Mujoco XML model, launch with:
  ```sh
  ros2 launch robosoccer_sim sim_mujoco.launch.py xml_path:=your_model.xml
  ```

## Example: Minimal End-to-End

```sh
# 1. Install dependencies (if not done)
pip install mujoco numpy

# 2. Source your ROS2 workspace
source install/setup.bash

# 3. Run the simulation
ros2 launch robosoccer_sim sim_mujoco.launch.py
```

---

For more information, see the Mujoco and ROS2 documentation.
