from setuptools import setup

package_name = 'robosoccer_motion'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['motion_planner_node'],
    install_requires=['setuptools', 'rclpy', 'geometry_msgs', 'std_msgs'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='Motion planner node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motion_planner_node = motion_planner_node:main',
        ],
    },
)
