from setuptools import setup

package_name = 'robosoccer_firmware'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['firmware_bridge_node'],
    install_requires=['setuptools', 'rclpy', 'std_msgs'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='Firmware bridge node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'firmware_bridge_node = firmware_bridge_node:main',
        ],
    },
)
