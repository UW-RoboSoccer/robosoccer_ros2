# RoboSoccer Mujoco Simulation

## Running the Mujoco Simulation

1. **Install dependencies** (if not already):
   ```sh
   pip install mujoco numpy rclpy
   ```
   Make sure you have Mujoco installed and a valid license if required. See [Mujoco installation](https://mujoco.readthedocs.io/en/stable/).

2. **Meshes**: Ensure all STL mesh files referenced in `robosoccer_sample.xml` are present in the `meshes/` directory.

3. **Launch the simulation**:
   ```sh
   ros2 launch robosoccer_sim sim_mujoco.launch.py
   ```
   This will start the Mujoco simulation and publish `/joint_states` and `/imu/data` topics.

4. **Customizing the model**:
   You can pass a different Mujoco XML file using a launch parameter:
   ```sh
   ros2 launch robosoccer_sim sim_mujoco.launch.py xml_path:=your_model.xml
   ```

5. **Controlling the robot**:
   Publish to the `/joint_command` topic (currently expects a `std_msgs/String`, but you may want to use a structured message).

6. **Extending**:
   - Edit `mujoco_sim_node.py` to improve command parsing, add sensor publishing, or connect to your control stack.
   - Add visualization or logging as needed.

---

For more information, see the Mujoco and ROS2 documentation.
