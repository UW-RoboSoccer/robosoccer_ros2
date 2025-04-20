from setuptools import setup

package_name = 'robosoccer_gamecontrol'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['gamecontrol_node'],
    install_requires=['setuptools', 'rclpy', 'std_msgs'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='GameController node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gamecontrol_node = gamecontrol_node:main',
        ],
    },
)
