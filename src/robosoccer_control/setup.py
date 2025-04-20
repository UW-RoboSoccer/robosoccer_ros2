from setuptools import setup

package_name = 'robosoccer_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['biped_controller_node'],
    install_requires=['setuptools', 'rclpy', 'std_msgs', 'geometry_msgs'],
    zip_safe=True,
    maintainer='YOUR_NAME',
    maintainer_email='YOUR_EMAIL',
    description='Biped controller node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'biped_controller_node = biped_controller_node:main',
        ],
    },
)
