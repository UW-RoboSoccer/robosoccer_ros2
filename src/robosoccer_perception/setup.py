from setuptools import setup

package_name = 'robosoccer_perception'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['sensor_node', 'perception_node'],
    install_requires=['setuptools', 'rclpy', 'sensor_msgs', 'geometry_msgs'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='Perception nodes for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_node = sensor_node:main',
            'perception_node = perception_node:main',
        ],
    },
)