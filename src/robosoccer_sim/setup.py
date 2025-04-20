from setuptools import setup

package_name = 'robosoccer_sim'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['mujoco_sim_node'],
    install_requires=['setuptools', 'rclpy', 'std_msgs', 'geometry_msgs', 'sensor_msgs', 'mujoco'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='MuJoCo simulation node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mujoco_sim_node = mujoco_sim_node:main',
        ],
    },
)
